# encoding=utf-8

import os
import unittest
from test.test_case.example_test_case import ExampleTestCase

base_project_path = os.path.dirname(__file__) + r'/'



def get_suit():
    suit = unittest.makeSuite(ExampleTestCase)
    return suit


if __name__ == '__main__':
    with open(base_project_path+'assets/log_files/automated_testing_runner_log.log', 'a+') as fp:
        runner = unittest.TextTestRunner(fp)
        runner.run(get_suit())