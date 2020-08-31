import logging
import logging.config

logging.config.fileConfig('./logging.conf')
logger = logging.getLogger('geofence')


# logging.basicConfig(filename='example.log',level=logging.INFO)

logging.debug('This message should go to the log file')
logging.warning('It\'s a warnning')  # will print a message to the console
logging.info('It\'s just a information')  # will not print anything