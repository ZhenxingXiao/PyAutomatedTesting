# coding=utf-8
from enum import Enum
from project import base_project_path
from config.configuration import ProjectConfig
from selenium import webdriver
from tools.log_factory import LogFactory


class WebDrivers(Enum):
    ChromeDiver = base_project_path+ProjectConfig().config['WEBDRIVER']['DRIVER_PATH']+'chromedriver.exe'
    FirefoxDriver = base_project_path+ProjectConfig().config['WEBDRIVER']['DRIVER_PATH']+'geckodriver.exe'


class DriverFactory():

    def __init__(self):
        self.logger = LogFactory.get_instance(self.__class__.__name__)
        config = ProjectConfig().config['WEBDRIVER']
        try:
            if config['DRIVER_NAME'] == 'ChromeDiver':
                self.driver = webdriver.Chrome(WebDrivers.ChromeDiver)
            elif config['DRIVER_NAME'] == 'FirefoxDriver':
                self.driver = webdriver.Firefox(WebDrivers.FirefoxDriver)
                raise NameError('web driver not found')
        except Exception as e:
            self.logger.debug('web driver not found')
