import logging 

class SetupLogger():

	def setup_logger(self):

	    logger = logging.getLogger(__name__)
	    logger.setLevel(logging.DEBUG)

	    streamlog = logging.StreamHandler()
	    filelog = logging.FileHandler('selenium_tests.log')
	    
	    streamlog.setLevel(logging.DEBUG)
	    filelog.setLevel(logging.DEBUG)

	    formatter = logging.Formatter("%(asctime)s %(levelname)-9s %(name)-8s %(thread)5s %(message)s")

	    filelog.setFormatter(formatter)
	    streamlog.setFormatter(formatter)

	    logger.addHandler(filelog)
	    logger.addHandler(streamlog)
	    
	    return logger