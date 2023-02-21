#!/usr/bin/env python
import sys
import os

import logging.config
from datetime import datetime

# root, dev
LOG_ENV = 'dev'
LOG_CONFIG_NAME = 'logging.conf'

# Folder save log file
FOLDER_SAVE_lOG = 'logs'
if not os.path.exists(FOLDER_SAVE_lOG):
    os.mkdir(FOLDER_SAVE_lOG)

log_path = ''
# current working directory path of script
if getattr(sys, 'frozen', False):
    # we are running in a bundle
    # log_path = sys._MEIPASS
    log_path = os.path.dirname(sys.executable)
else:
    # we are running in a normal Python environment
    log_path = os.path.dirname(os.path.abspath(__file__))

log_path = log_path + '/' + LOG_CONFIG_NAME

logging.config.fileConfig(log_path)
log = logging.getLogger(LOG_ENV)

fh = logging.FileHandler(FOLDER_SAVE_lOG + '/' +
                         '{:%Y-%m-%d}.log'.format(datetime.now()), encoding="UTF-8")
formatter = logging.Formatter(
    '%(asctime)s | %(name)-4s | %(levelname)-8s | %(filename)s | %(lineno)04d | %(funcName)s | %(message)s')
fh.setFormatter(formatter)
log.addHandler(fh)


# TEST
# log.info('test log info')
# log.debug('test log debug')
# log.warning('test log warning')
# log.error('test log error')
