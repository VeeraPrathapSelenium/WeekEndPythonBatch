import logging

logging.basicConfig(filename='Logging.log',format='%(asctime)s %(message)s %(lineno)d')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.debug("Hello i am debug level")
logging.info("Hello i am info level")
logging.warning("Hello i am warning level")
logging.error("Hello i am error level")
logging.critical("Hello i am critical level")
