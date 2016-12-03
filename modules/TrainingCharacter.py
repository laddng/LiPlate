import cv2;
import logging;
from logging.config import fileConfig;
from copy import copy, deepcopy;

# logging setup
fileConfig("logging_config.ini");
logger = logging.getLogger();

class TrainingCharacter:
	""" Training Character class to use for OCR """
	def __init__(self, character, image):
		self.character = character[:1];
		self.character_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
		logger.info("Training character object created for %s", character);

