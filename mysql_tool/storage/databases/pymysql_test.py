# -*- coding: utf-8 -*-

"""
Create by Mr.hao on 2020/12/12.
"""

from mysql_tool.entity.storage import Storage


class SqlTest(Storage):
    db_flag = "bdp_spider"

    def __init__(self, *args, **kwargs):
        super(SqlTest, self).__init__(*args, **kwargs)

    def select_data(self):
        sql = "SELECT * FROM url_seed limit 1"
        return self.fetchone_data(sql, [], cursor_type=True)

    def load_new_links_2(self, limit):
        sql = "SELECT * FROM url_type limit %s;"
        return self.fetchall_data(sql, [limit], cursor_type=True)

    def insert_data_to_items_info(self, req):
        sql = "INSERT IGNORE INTO " \
              "items_info " \
              "(url, url_md5, referer, site, found_time, is_update, weight, task_id," \
              " batch_id, create_time, source, url_type_id, channel, item_url, list_rowkey) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        self.execute_sql(sql, req)

    def update_data_to_items_info(self, req):
        sql = "UPDATE items_info " \
              "SET retry = %s, status = %s, update_time=%s " \
              "WHERE url_md5 = %s;"
        return self.execute_sql(sql, req)
