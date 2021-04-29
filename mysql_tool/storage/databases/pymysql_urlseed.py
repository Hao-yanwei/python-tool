# -*- coding: utf-8 -*-

"""
Create by Mr.hao on 2020/12/12.
"""

from mysql_tool.entity.storage import Storage




class Urlseed(Storage):

    db_flag = "bdp_spider"

    def __init__(self, *args, **kwargs):
        super(Urlseed, self).__init__(*args, **kwargs)

    def selectUrlseed(self):
        sql = "SELECT * FROM url_seed limit 1"
        return self.fetchone_data(sql, [], cursor_type=True)

    def load_new_links_2(self, limit):
        sql = "SELECT * FROM url_type limit %s;"
        return self.fetchall_data(sql, [limit], cursor_type=True)
