import cv2;
import numpy as np;
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

def showResults():
	plt.figure(0);

	for image in Image.images:
		plt.subplot(211);
		plt.plot(image.image_file);
		plt.show();

	return True;

