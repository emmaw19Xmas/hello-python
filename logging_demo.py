# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/16/2021 10:45 PM
# @Function:

import logging
#logging 默认设置的级别是warning，所以等级低于warning的日志都不会被打印。
logging.basicConfig(filename='example.log',  level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -%(message)s')
logging.warning("watch out")
logging.info('I told you so')
print("=================================================")
# logging.basicConfig(level=logging.DEBUG) 一定要写在最前面才能有用
logging.debug('Some debugging details.')
logging.info('The logging module is working')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')