# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
import sqlite3

#workflow: scraped data -> Item Container -> Pipeline -> SQL Database

class ScraperPipeline(object):

    def __init__(self):
        self.create_connection()
        #self.create_cat_table
        #self.create_list_table

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='a2009121126',
            port=3306,
            database = 'vanc_yp'
        )
        #self.conn = sqlite3.connect('mydb1.db')
        self.curr = self.conn.cursor()

        #self.curr.execute(""" DROP TABLE IF EXISTS 'wt_yp_sub_cat' """)
        self.curr.execute(""" CREATE TABLE IF NOT EXISTS wt_yp_sub_cat (
                    main_cat_id text, 
                    c_name text, 
                    e_name text, 
                    update_time text
                    )""")

        #self.curr.execute(""" DROP TABLE IF EXISTS 'wt_yp_listing' """)
        self.curr.execute(""" CREATE TABLE IF NOT EXISTS wt_yp_listing (
                    contact_phone text,
                    title text, 
                    contact_name text, 
                    contact_email text,
                    contact_addr text, 
                    cover_pic text, 
                    description text, 
                    update_time text, 
                    sub_cat_id text
                    )""")
    
    #create table for categories
    def create_cat_table(self):
        #self.curr.execute(""" DROP TABLE IF EXISTS 'wt_yp_sub_cat' """)
        self.curr.execute(""" CREATE TABLE 'wt_yp_sub_cat' (
                    main_cat_id text, 
                    c_name text, 
                    e_name text, 
                    update_time text
                    )""")
    
    #create table for the info of each categories
    def create_list_table(self):
        #self.curr.execute(""" DROP TABLE IF EXISTS 'wt_yp_listing' """)
        self.curr.execute(""" CREATE TABLE 'wt_yp_listing' (
                    contact_phone text,
                    title text, 
                    contact_name text, 
                    contact_email text,
                    contact_addr text, 
                    cover_pic text, 
                    description text, 
                    update_time text, 
                    sub_cat_id text
                    )""")


    def process_item(self, item, spider):
        self.create_connection()
        #self.create_cat_table
        #self.create_list_table
        self.store_db(item)
        return item


    def store_db(self, item):
        e_name = ''

        if not item['contact_phone']  :
            contact_phone = ''
        else:
            contact_phone = item['contact_phone'][0] 

        if not item['contact_name']  :
            contact_name = ''
        else:
            contact_name = item['contact_name'][0]

        if not item['contact_email'] :
            contact_email = ''
        else:
            contact_email = item['contact_email'][0]

        if not item['contact_addr']  :
            contact_addr = ''
        else:
            contact_addr = item['contact_addr'][0]

        if not item['cover_pic']  :
            cover_pic = ''
        else:
            cover_pic = item['cover_pic'][0]

        if not item['description']  :
            description = ''
        else:
            description = item['description'][0]

        if not item['sub_cat_id']  :
            sub_cat_id = ''
        else:
            sub_cat_id = item['sub_cat_id'][0]

        if not item['main_cat_id']  :
            main_cat_id = ''
        else:
            main_cat_id = item['main_cat_id'][0]

        if not item['c_name']  :
            c_name = ''
        else:
            c_name = item['c_name'][0]

        if not item['title'] :
            title = ''
        else:
            title = item['title'][0]


        self.curr.execute(
            """ insert into wt_yp_sub_cat values (%s,  %s,  %s,  %s) """, (
                main_cat_id,
                c_name,
                e_name,
                '',
            ))

        self.curr.execute(""" insert into wt_yp_listing values ( %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s) """, (
            contact_phone,
            title,
            contact_name,
            contact_email,
            contact_addr,
            cover_pic,
            description,
            '',
            sub_cat_id,
        ))

        self.conn.commit()



