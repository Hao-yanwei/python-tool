# -*- coding: utf-8 -*-

"""
 Created by Mr.Hao on 2018/8/3.
"""

from utils import get_logger
from utils.retry import Retry
# from MySQLdb.cursors import DictCursor
from pymysql.cursors import DictCursor
from entity.dbService import database_service


class Storage(object):

    db_flag = None
    log = get_logger("Storage")

    def __init__(self, *args, **kwargs):
        pass

    @Retry(max_retries=2, return_on_failure=False)
    def execute_sql(self, sql, req):
        if not self.db_flag:
            self.log.warn("this db_flag is none, please, check db config from config_local.py")
            return False
        connection = database_service.get_connection(self.db_flag)
        cursor = connection.cursor()
        return cursor.execute(sql, req)

    @Retry(max_retries=2, return_on_failure=False)
    def execute_multi_sql(self, sql, req):
        if not self.db_flag:
            self.log.warn("this db_flag is none, please, check db config from config_local.py")
            return []

        connection = database_service.get_connection(self.db_flag)
        cursor = connection.cursor()
        cursor.executemany(sql, req)
        return True

    @Retry(max_retries=2, return_on_failure=[])
    def fetchall_data(self, sql, req, cursor_type=None):
        if not self.db_flag:
            self.log.warn("this db_flag is none, please, check db config from config_local.py")
            return []
        connection = database_service.get_connection(self.db_flag)
        cursor = connection.cursor()
        if cursor_type:
            cursor = connection.cursor(DictCursor)
        cursor.execute(sql, req)
        return cursor.fetchall()

    @Retry(max_retries=2, return_on_failure=[])
    def fetchone_data(self, sql, req, cursor_type=None):
        if not self.db_flag:
            self.log.warn("this db_flag is none, please, check db config from config_local.py")
            return []

        connection = database_service.get_connection(self.db_flag)
        cursor = connection.cursor()
        if cursor_type:
            cursor = connection.cursor(DictCursor)

        cursor.execute(sql, req)
        return cursor.fetchone()

