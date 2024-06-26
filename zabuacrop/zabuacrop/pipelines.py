# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

class ZabuacropPipeline:

    def __init__(self) -> None:
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = os.getenv("host"),
            user = os.getenv("user"),
            password = os.getenv("password"),
            database = os.getenv("database")
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" CREATE TABLE IF NOT EXISTS companydata_2024(
                          company_title varchar(255),
                           cin_number varchar(255),
                          roc_name varchar(255),
                          status varchar(255))""")
        
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self,item):
        self.curr.execute("""INSERT into companydata_2024 values (%s,%s,%s,%s)
                          """ , (item['company_title'],
                                 item['cin_number'],
                                 item['roc_name'],
                                 item['status']))
        self.conn.commit()

    def close_spider(self, spider):

        self.cur.close()
        self.conn.close()

