import scrapy
from ..items import CategoryItem

class VancSpider(scrapy.Spider):
    name = 'Vanc'
    start_urls = ['https://c.vanpeople.com/yellowpage.html']

    def parse(self, response):
        cats = CategoryItem()
        for links in response.css('div.yp_box dd a'):
            #attributes of the categories
            main_cat_id= links.css('a::text').extract()
            c_name = links.css('a::text').extract()
            e_name = ''
            update_time = ''
            url = 'https://c.vanpeople.com/' + ''.join(links.css('a::attr(href)').extract())

            cats['main_cat_id'] = main_cat_id
            cats['c_name'] = c_name
            cats['e_name'] = e_name
            cats['update_time'] = update_time

            cats['contact_phone'] = ''
            cats['title'] = ''
            cats['contact_name'] = ''
            cats['contact_email'] = ''
            cats['contact_addr'] = ''
            cats['cover_pic'] = ''
            cats['description'] = ''
            cats['update_time'] = ''
            cats['sub_cat_id'] = ''

            #load into database
            yield cats
            #access inside content
            yield scrapy.Request(url, callback=self.parse_link)
    
    ###################################################################
    def parse_link(self, response):
        for item in response.css('li.list'):
            #attributes of the links
            link = 'https://c.vanpeople.com/' + ''.join(item.css('a.yp-list-title').attrib['href'])

            #get into the page for more details
            yield scrapy.Request(link, callback=self.parse_detail)

    #get detail info and save it into database
    def parse_detail(self, response):
        cats = CategoryItem()

        title = response.css('div.info-content-title h1::text').get()

        try:
            contact_phone = response.css('div.tel p::text').get()
            contact_name = response.css('div.yp_detail_line span::text').extract()[0]
            contact_email = response.css('div.yp_detail_line span::text').extract()[1]
            contact_addr = response.css('div.yp_detail_line span::text').extract()[2]
            cover_pic = 'https://c.vanpeople.com/' + ''.join(response.css('img.lazy_info').attrib['data-original'])
            description = response.css('article.info-detail-content').extract()
            sub_cat_id = response.css('div.crumb a::text').extract()[1]

        except:
            contact_phone = ''
            contact_name = ''
            contact_email = ''
            contact_addr = ''
            cover_pic = ''
            description = ''
            sub_cat_id = ''

        update_time = ''

        cats['main_cat_id'] = ''
        cats['c_name'] = ''
        cats['e_name'] = ''
        cats['update_time'] = ''

        cats['contact_phone'] = contact_phone
        cats['title'] = title
        cats['contact_name'] = contact_name
        cats['contact_email'] = contact_email
        cats['contact_addr'] = contact_addr
        cats['cover_pic'] = cover_pic
        cats['description'] = description
        cats['update_time'] = update_time
        cats['sub_cat_id'] = sub_cat_id

        #load into database
        yield cats


            
