""" Configuration
With basicConfig(**kwargs) you can customize the root logger. The most common parameters are the level, the format, and the filename. See https://docs.python.org/3/library/logging.html#logging.basicConfig for all possible arguments. See also https://docs.python.org/3/library/logging.html#logrecord-attributes for possible formats and https://docs.python.org/3/library/time.html#time.strftime how to set the time string. Note that this function should only be called once, and typically first thing after importing the module. It has no effect if the root logger already has handlers configured. For example calling logging.info(...) before the basicConfig will already set a handler. """


import logging

#TODO:

""" logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S') """

#TODO:
#import helper #propagate False HACE QUE no nada se bloquee y se propaga a nuestro registro basico

#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')

# Now also debug messages will get logged with a different format.
#logging.debug('Debug message')

""" LogHandlers
Handler objects are responsible for dispatching the appropriate log messages to the handler's specific destination. For example you can use different handlers to send log messaged to the standard output stream, to files, via HTTP, or via Email. Typically you configure each handler with a level (setLevel()), a formatter (setFormatter()), and optionally a filter (addFilter()). See https://docs.python.org/3/howto/logging.html#useful-handlers for possible built-in handlers. Of course you can also implement your own handlers by deriving from these classes. """

#TODO:
""" logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#level and the format 
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_h.setFormatter(stream_format)
file_h.setFormatter(file_format)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is a error')
 """

#TODO:
""" import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')
logger.debug('this is a debug messager') """

#TODO:

""" try:
  a = [1,2,3,4,5]
  val = a[7]
except IndexError as e:
  logging.error(e, exc_info=True)


import traceback

try:
  a = [1,2,3,4,5]
  val = a[8]
except IndexError as e:
  logging.error('the error is %s', traceback.format_exc()) """ 

#TODO: 
""" from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello, world!')
"""  
    
import time
from logging.handlers import TimedRotatingFileHandler
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) 

# This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
logger.addHandler(handler)
 
for _ in range(6):
    logger.info('Hello, world!')
    time.sleep(5)