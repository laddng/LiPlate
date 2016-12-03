import cv2;
import os;
from modules.Plate import *;
from modules.TrainingCharacter import *;
import logging;
from logging.config import fileConfig;

fileConfig("logging_config.ini");
logger = logging.getLogger();

""" Loads all the images of cars from `/images/cars/` """
def loadImages(folder):
	plates_array = [];
	for image_filename in os.listdir(folder):
		logger.info("Loading image %s...", image_filename);
		image_file = cv2.imread(folder+image_filename);
		plateObject = Plate(image_file);
		plates_array.append(plateObject);
	return plates_array;

""" Loads all the character training images from `images/characters` """
def loadCharacters(folder):
	characters_array = [];
	for character in os.listdir(folder):
		logger.info("Loading character %s...", character);
		character_file = cv2.imread(folder+character);
		trainingCharacterObject = TrainingCharacter(character, character_file);
		characters_array.append(trainingCharacterObject);
	return characters_array;

