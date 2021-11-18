# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/17/2021 8:48 PM
# @Function:

import logging.config
logging.config.fileConfig("logger.conf")
logger = logging.getLogger("main")

logger.debug("这是一个debug语句")
