import logging.config

if __name__ == "__main__":
    logging.config.fileConfig('./config/logging.conf', disable_existing_loggers=False)
    logger = logging.getLogger(__name__)

    logger.info('App started')
