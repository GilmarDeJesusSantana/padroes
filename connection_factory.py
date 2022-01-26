# -*- coding: UTF-8 -*-
import MySQLdb


class Connection_Factory():
    def get_connection(self):
        connection = MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='',
            db='alura')
        return connection
