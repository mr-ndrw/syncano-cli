import logging

__title__ = 'Syncano CLI'
__version__ = '1.0.0'
__author__ = 'Daniel Kopka'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Syncano'
VERSION = __version__


console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(console_formatter)

logger = logging.getLogger('syncanocli')
logger.addHandler(console_handler)