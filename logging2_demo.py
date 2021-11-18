# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/17/2021 8:13 PM
# @Function:
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.WARNING)

# create console handler and set level to debug
#ch = logging.StreamHandler()#流处理器-将log输出到terminal里；
ch = logging.FileHandler("example2.log", encoding="utf-8") #文件处理器，输出到文件里
ch.setLevel(logging.WARNING)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')