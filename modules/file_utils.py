import cv2;
import os;
from modules.plate import *;
import logging;
from logging.config import fileConfig;

fileConfig("logging_config.ini");
logger = logging.getLogger();

def loadImages(folder):
	plates_array = [];
	for image_filename in os.listdir("images/cars/"):
		logger.info("Loading image %s...", image_filename);
		image_file = cv2.imread("images/cars/"+image_filename);
		plateObject = Plate(image_file);
		plates_array.append(plateObject);

	return plates_array;

