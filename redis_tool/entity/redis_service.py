# -*- coding: utf-8 -*-

"""
 Created by haoyanwei on 2018/9/25.
"""

import redis
import config


class RedisService(object):

    pools = {}

    def __init__(self, *args, **kwargs):
        super(RedisService, self).__init__(*args, **kwargs)

    def get_client(self, name):
        if name not in self.pools:
            self.pools[name] = redis.ConnectionPool(**config.CACHES[name])
        return redis.Redis(connection_pool=self.pools[name])
