#!/usr/bin/env python

import logging
import sys

"""
======================= START CONFIG LOG
"""
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s',
                              '%m-%d-%Y %H:%M:%S')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)
"""
======================= END CONFIG LOG
"""

# TEST
# logger.info('test log info')
# logger.debug('test log debug')
# logger.warning('test log warning')
# logger.error('test log error')
