# coding=utf-8

from unittest import TestCase
from time import sleep
from tools.driver_factory import DriverFactory
from tools.log_factory import LogFactory
from test.page.sub_pages.login_page import LoginPage


class ExampleTestCase(TestCase):
    def setUp(self):
        self.driver = DriverFactory.driver()
        self.baseUrl = "https://www.baidu.com"
        self.logger = LogFactory.get_instance(self.__class__.__name__)

    def tearDown(self):
        self.driver.close()

    def test_login(self):
        self.logger.info('----------------start testing----------------')
        example_page = LoginPage(self.driver, self.baseUrl)
        self.logger.info('----------------open page----------------')
        example_page.login()
        sleep(10)
        self.logger.info('----------------end testing----------------')