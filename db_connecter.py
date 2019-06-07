import pymysql
from constant import *


class DatabaseConnecter:

    def __init__(self):
        self.conn = pymysql.connect(host=DATABASE_ENDPOINT,
                                    user=DATABASE_USER,
                                    password=DATABASE_PASSWORD,
                                    db=DATABASE_NAME,
                                    charset='utf8')
        self.curs = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def insert(self, itemList):
        sql = """insert into musinsa(title,img_url,link,description)
                 values (%s, %s, %s, %s)"""
        for item in itemList:
            self.curs.execute(sql, (item['title'], item['img_url'],
                                    item['link'], item['description']))

        self.conn.commit()
