from modules.file_utils import *;
from modules.Plate import *;
from modules.TrainingCharacter import *;
import logging;
from logging.config import fileConfig;

fileConfig("logging_config.ini");
logger = logging.getLogger();

def run():

	plates_array = loadImages("images/cars/");
	characters_array = loadCharacters("images/characters/");
	logger.info("All testing images and characters have been downloaded.");

	for plate in plates_array:
		plate.plateSearch(characters_array);

	logger.info("Finished plate recognition.");
	return True;

run();

