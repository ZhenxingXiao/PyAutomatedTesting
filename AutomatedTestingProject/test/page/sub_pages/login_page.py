# coding=utf-8

from tools.log_factory import LogFactory
from test.page.base_page import BasePage
from time import sleep
from selenium import webdriver


class LoginPage(BasePage):
    logger = LogFactory.get_instance(__name__)

    def __init__(self, driver, base_url):
        BasePage.__init__(self, driver, base_url)
        self.driver = driver if driver is not None else webdriver.Chrome()

    def login(self):
        self.open_main_page()
        self.logger.debug('click login link')
        a = self.driver.find_element_by_css_selector("[name='tj_login']")
        self.logger.debug(a.get_attribute("text"))
