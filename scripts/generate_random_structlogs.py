import logging
import random
import sys
import time

import structlog
from structlog.stdlib import LoggerFactory
from essential_generators import DocumentGenerator

logging.basicConfig()

structlog.configure(logger_factory=LoggerFactory())  

logger = structlog.get_logger()

#log.warning("it works!", difficulty="easy")  
#WARNING:structlog...:difficulty='easy' event='it works!'

generator=DocumentGenerator()
logmethods=[logger.warning,
            logger.info,
            logger.debug,
            logger.error,
            logger.fatal]
while True:
    logmethod=random.choice(logmethods)
    logmethod(generator.sentence(),say=1,do_not_this="at home")
    time.sleep(random.random()/100)
