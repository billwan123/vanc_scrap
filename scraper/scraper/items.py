# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy_djangoitem import DjangoItem
#from properties.models import Category
#from properties.models import Info


class CategoryItem(scrapy.Item):
    # define the fields for your item here like:
    main_cat_id = scrapy.Field()
    c_name = scrapy.Field()
    e_name = scrapy.Field()
    update_time = scrapy.Field()

    contact_phone = scrapy.Field()
    title = scrapy.Field()
    contact_name = scrapy.Field()
    contact_email = scrapy.Field()
    contact_addr = scrapy.Field()
    cover_pic = scrapy.Field()
    description = scrapy.Field()
    update_time = scrapy.Field()
    sub_cat_id = scrapy.Field()
