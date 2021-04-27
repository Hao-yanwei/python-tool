# -*- coding: utf-8 -*-

import logging.config
import logging.handlers

def get_logger(logger_name):
    logging.basicConfig(format="[%(asctime)s] %(filename)s: %(lineno)s: "
                               "%(levelname)s: %(threadName)s: %(name)s: %(message)s", level=logging.INFO)
    return logging.getLogger(logger_name)