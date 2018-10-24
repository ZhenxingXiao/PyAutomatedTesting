# coding=utf-8

import logging
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
from config.configuration import ProjectConfig
from __project__path__ import base_project_path


class LogFactory:

    @staticmethod
    def get_instance(name):
        pc = ProjectConfig()
        log_config = pc.config['LOG']

        logger = logging.getLogger(name=name)
        logger.setLevel(log_config['LEVEL'])

        fmt = logging.Formatter(fmt=log_config['FMT'])
        sh = logging.StreamHandler()
        sh.setFormatter(fmt=fmt)
        logger.addHandler(sh)
        if 'SF' in log_config['HANDLER']:
            sf_handler = logging.FileHandler(
                filename=base_project_path+log_config['FILE_PATH']+log_config['FILE_NAME'],
                encoding=log_config['ENCODING']
            )
            sf_handler.setFormatter(fmt=fmt)
            logger.addHandler(sf_handler)
        if 'TR' in log_config['HANDLER']:
            tr_handler = TimedRotatingFileHandler(
                filename=base_project_path+log_config['TIMED_MULTI_FILES'],
                when=log_config['WHEN'],
                backupCount=int(log_config['TIME_BACKUPCOUNT']),
                interval=int(log_config['INTERVAL']),
                encoding=log_config['ENCODING']
            )
            tr_handler.setFormatter(fmt=fmt)
            logger.addHandler(tr_handler)
        if 'RF' in log_config['HANDLER']:
            tr_handler = RotatingFileHandler(
                filename=base_project_path + log_config['SIZED_MULTI_FILES'],
                maxBytes=int(log_config['MAXBYTES']),
                backupCount=int(log_config['SIZE_BACKUPCOUNT']),
                encoding=log_config['ENCODING']
            )
            tr_handler.setFormatter(fmt=fmt)
            logger.addHandler(tr_handler)
        return logger


if __name__ == '__main__':
    logger = LogFactory.get_instance(__file__)
    logger.debug('xy' in 'fnwiufixyfase')