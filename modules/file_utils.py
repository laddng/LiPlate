import cv2;
import os;
from modules.plate import *;

def loadImages(folder):
	plates_array = [];
	for image_filename in os.listdir("images/cars/"):
		print("[loadImages]: Loading image "+image_filename+"...");
		image_file = cv2.imread("images/cars/"+image_filename);
		plateObject = Plate(image_file);
		plates_array.append(plateObject);

	return plates_array;

