from modules.file_utils import *;
from modules.plate import *;
import logging;
from logging.config import fileConfig;

fileConfig("logging_config.ini");
logger = logging.getLogger();

def run():

	plates_array = loadImages("images/cars/");
	logger.info("All testing images have been downloaded.");

	for plate in plates_array:
		plate.plateSearch();

	logger.info("Finished plate recognition.");
	return True;

run();

