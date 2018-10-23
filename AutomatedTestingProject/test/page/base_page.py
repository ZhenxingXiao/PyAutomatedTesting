# coding=utf-8

from tools.log_factory import LogFactory


class BasePage():

    def __init__(self, driver, base_url):
        self.logger = LogFactory.get_instance(self.__class__.__name__)
        self.driver = driver
        self.base_url = base_url

    def openMainPage(self):
        try:
            self.driver.get(self.base_url)
            self.driver.implicitly_wait(30)
        except Exception as e:
            self.logger.error('can not open the main page')