# coding=utf-8

from configparser import ConfigParser
from __project__path__ import base_project_path


class ProjectConfig:
    config_dir = 'config/project.cfg'
    config = {}

    def __init__(self):
        cp = ConfigParser()
        cp.read(base_project_path+self.config_dir)
        for section in cp.sections():
            self.config[section.upper()] = {}
            for option in cp.options(section=section):
                temp = cp.get(section=section, option=option)
                if option == 'fmt':
                    temp = self.resolve_fmt(temp)
                self.config[section.upper()][option.upper()] = temp

    @classmethod
    def resolve_fmt(cls, old_fmt):
        arr_old_fmt = old_fmt.split('-')
        arr_new_fmt = []
        for st in arr_old_fmt:
            if st == "lineno":
                arr_new_fmt.append('%(' + st + ')d')
            else:
                arr_new_fmt.append('%('+st+')s')
        return "-".join(arr_new_fmt)
