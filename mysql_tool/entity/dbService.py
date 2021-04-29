# -*- coding: utf-8 -*-
"""
 Created by Dr.Hao on 2017/8/8
"""


import pymysql
# from DBUtils.PooledDB import PooledDB
from mysql_tool import config
from dbutils.pooled_db import PooledDB


class DatabaseService(object):

    pools = {}

    def __init__(self, database_configs, max_connection=8):
        self.database_configs = database_configs
        self.max_connection = max_connection

    @staticmethod
    def closed(connection):
        try:
            connection.close()
        except:
            pass

    def get_connection(self, name):
        if name not in self.pools:
            self.pools[name] = PooledDB(
                pymysql, maxconnections=self.max_connection, charset="utf8", autocommit=True,
                **self.database_configs[name])
        return self.pools[name].connection()


database_service = DatabaseService(config.DATABASES, config.MAX_DB_CONNECTIONS)

