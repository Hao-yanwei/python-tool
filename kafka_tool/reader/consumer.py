# -*- coding: utf-8 -*-

"""
 Created by hao on 2018/10/24.
"""

import sys
import copy
import time
import traceback
from kafka_tool import topics
from kafka_tool import get_logger
from kafka_tool.base import Baser


logger = get_logger("Consumer")


class Consumer(Baser):

    _MESSAGE_NAME = topics.KFK_TOPIC

    def __init__(self, *args, **kwargs):
        super(Consumer, self).__init__(groupId="download")

    @property
    def get_localtime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def receive_message(self):
        consumer = self._consumer
        for msg in consumer:
            offset, value = msg.offset, msg.value
            logger.info("now, get msg, for offset: %s, value: %s, start", offset, value)
            try:
                pass
            except:
                # 打印每一处错误
                t, v, tb = sys.exc_info()
                logger.error("has error, %s, %s, %s" % (t, v, traceback.format_tb(tb)))
            logger.info("this msg is done....")
