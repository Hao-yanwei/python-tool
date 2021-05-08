# -*- coding: utf-8 -*-

"""
 Created by haoyanwei on 2018/11/6.
"""

import datetime
from apscheduler.schedulers.background import BackgroundScheduler


class BaseScheduler(object):

    default_interval = 2
    default_second = 30
    default_month = "1-3,7-9"
    default_day = "1"
    default_hour = "1"
    executor = BackgroundScheduler(timezone="Asia/Shanghai")

    def __init__(self):
        super(BaseScheduler, self).__init__()

    @property
    def get_first_run_time(self):
        return datetime.datetime.now() + datetime.timedelta(seconds=+60)

    def service(self):
        pass

    def interval_start(self):
        kwargs = dict()
        kwargs['minutes'] = self.default_interval
        kwargs['start_date'] = self.get_first_run_time

        self.executor.add_job(self.service, 'interval', max_instances=1, **kwargs)
        self.executor.start()

    def cron_start(self):
        kwargs = dict()
        kwargs['month'] = self.default_month
        kwargs['day'] = self.default_day
        kwargs['hour'] = self.default_hour
        kwargs['second'] = self.default_second
        kwargs['start_date'] = self.get_first_run_time

        self.executor.add_job(self.service, 'cron', max_instances=1, **kwargs)
        self.executor.start()

    def date_start(self):
        kwargs = dict()
        kwargs['run_date'] = '2009-11-06 16:30:05'

        self.executor.add_job(self.service, 'date', max_instances=1, **kwargs)
        self.executor.start()
