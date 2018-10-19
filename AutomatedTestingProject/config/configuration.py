# coding=utf-8

import os
import logging
from configparser import ConfigParser
import schedule
import time


class TestClass():
    def test_fun(self):
        logger = logging.getLogger(self.__class__.__name__)
        fmt = '%(asctime)s - %(filename)s - %(name)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s'
        logger.setLevel(logging.DEBUG)
        sh = logging.StreamHandler()
        sh.setFormatter(logging.Formatter(fmt))
        logger.addHandler(sh)
        logger.debug('hello world')


def job():
    print('working')


if __name__ == '__main__':
    tc = TestClass()
    schedule.every(5).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

