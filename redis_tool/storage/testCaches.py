# -*- coding: utf-8 -*-

"""
Create by Mr.zhang on 2020/3/17.

"""
from redis_tool.entity.redis_service import RedisService


class TestCaches(object):

    cache_flag = "TestCaches"
    redis = RedisService()

    def __init__(self, *args, **kwargs):
        super(TestCaches, self).__init__(*args, **kwargs)

    def set_url_cache(self, url):
        client = self.redis.get_client(self.cache_flag)
        return client.sadd("askbob_url", url)

    def is_existed(self, url):
        client = self.redis.get_client(self.cache_flag)
        return client.sismember("askbob_url", url)

    def delete_key(self):
        client = self.redis.get_client(self.cache_flag)
        client.delete("askbob_url")

    def exists_key(self):
        client = self.redis.get_client(self.cache_flag)
        return client.exists("askbob_url")