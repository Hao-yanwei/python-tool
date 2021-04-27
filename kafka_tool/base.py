# -*- coding: utf-8 -*-

"""
 Created by hao on 2018/10/24.
"""
import sys
import json
import traceback
from kafka_tool import get_logger
from kafka.errors import KafkaError
from kafka import KafkaProducer, KafkaConsumer

logger = get_logger("base")


class Baser(object):
    _MESSAGE_NAME = '_base'

    KAFKA_HOSTS = ["10.28.5.87:9092", "10.28.5.88:9092", "10.28.5.89:9092"]

    def __init__(self, groupId=None):
        self.client_id = "8eaa8c81edfd41f28a50f9121ad14572"
        self._producer = KafkaProducer(
            bootstrap_servers=self.KAFKA_HOSTS,
            max_request_size=10485760,
            # 传输时的压缩格式
            compression_type="gzip",
            # 每条消息的最大大小
            # max_request_size=1024 * 1024 * 20,
            client_id=self.client_id,
            # 重试次数
            retries=3,
        )
        self._consumer = KafkaConsumer(
            self._MESSAGE_NAME,
            bootstrap_servers=self.KAFKA_HOSTS,
            # bootstrap_servers="10.26.241.67:9092,10.26.241.68:9092,10.26.241.69:9092",
            # earliest
            # 当各分区下有已提交的offset时，从提交的offset开始消费；无提交的offset时，从头开始消费
            # latest
            # 当各分区下有已提交的offset时，从提交的offset开始消费；无提交的offset时，消费新产生的该分区下的数据
            # none
            # topic各分区都存在已提交的offset时，从offset后开始消费；只要有一个分区不存在已提交的offset，则抛出异常
            auto_offset_reset='earliest',
            client_id=self.client_id,
            group_id=groupId,
            # 若不指定 consumer_timeout_ms，默认一直循环等待接收，若指定，则超时返回，不再等待
            # consumer_timeout_ms ： 毫秒数
        )

    def get_message_name(self):
        return self._MESSAGE_NAME

    def send(self, msg, partition=None, times=0):

        if times > 3:
            logger.error('this %s, msg: %s, lost...', self._MESSAGE_NAME, msg)
            return False

        try:
            producer = self._producer
            # 发送到指定的消息主题（异步，不阻塞）
            record_metadata = producer.send(self._MESSAGE_NAME, value=msg, partition=partition)
            # 获取发送结果（阻塞），超时时间为空则一直等待
            record_metadata = record_metadata.get(timeout=60)
            logger.info("*" * 100)
            logger.info("writer msg partition: %s", record_metadata.partition)
            logger.info("writer msg offset: %s", record_metadata.offset)
            logger.info("writer msg: %s", msg)
            producer.flush()
            return True
        except KafkaError as e:
            t, v, tb = sys.exc_info()
            logger.error("send msg ext has error, please check: %s, %s, %s", t, v, traceback.format_tb(tb))
            if self._producer:
                del self._producer
                self.get_producer()
            # 重试机制
            return self.send(msg, None, times + 1)

    def receive_message(self):
        """
        ex:
        for message in self.get_consumer():
            print json.loads(message.value)

        """

    @staticmethod
    def str_to_json(msg):
        return json.loads(msg)

    @staticmethod
    def json_to_str(msg):
        return json.dumps(msg, ensure_ascii=False, encoding="utf-8")
