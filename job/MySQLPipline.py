# -*-coding:utf-8-*-
import pymysql.cursors


class MySQLPipeline(object):
    def __int__(self):
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='job',  # 数据库名
            user='root',  # 数据库用户名
            passwd='root',  # 数据库密码
            charset='utf8mb4',  # 编码方式
            use_unicode=True)
        self.cursor = self.connect.cursor()
