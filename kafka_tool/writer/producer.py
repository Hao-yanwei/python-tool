# -*- coding: utf-8 -*-

"""
 Created by hao on 2018/10/24.
"""

from kafka_tool import topics
from kafka_tool import get_logger
from kafka_tool.base import Baser


logger = get_logger("Producer")


class Producer(Baser):

    _MESSAGE_NAME = topics.KFK_TOPIC

    def sendMsg(self, msg):
        self.send(msg)
