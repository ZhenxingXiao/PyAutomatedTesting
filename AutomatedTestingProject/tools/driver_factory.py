# coding=utf-8
from enum import Enum
from config.configuration import ProjectConfig
from selenium import webdriver
from tools.log_factory import LogFactory
from __project__path__ import base_project_path


class WebDrivers(Enum):
    ChromeDiver = base_project_path+ProjectConfig().config['WEBDRIVER']['DRIVER_PATH']+'chromedriver.exe'
    FirefoxDriver = base_project_path+ProjectConfig().config['WEBDRIVER']['DRIVER_PATH']+'geckodriver.exe'


class DriverFactory():

    @staticmethod
    def driver():
        logger = LogFactory.get_instance('DriverFactory')
        config = ProjectConfig().config['WEBDRIVER']
        try:
            if config['DRIVER_NAME'] == 'ChromeDriver':
                return webdriver.Chrome(WebDrivers.ChromeDiver.value)
            elif config['DRIVER_NAME'] == 'FirefoxDriver':
                return webdriver.Firefox(WebDrivers.FirefoxDriver.value)
        except Exception as e:
            logger.debug('web driver not found')