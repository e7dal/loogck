import logging
import random
import sys
import time

from essential_generators import DocumentGenerator

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logmethods=[logging.warning,
            logging.info,
            logging.debug,
            logging.error,
            logging.fatal]

generator=DocumentGenerator()
while True:
    logmethod=random.choice(logmethods)
    s=generator.sentence()
    s=' '.join(s.splitlines())
    logmethod(s)
    time.sleep(random.random()/1000)
