import cv2;
import os;
from modules.plate import *;
from modules.classifier import *;

def loadImages(folder, object_type):
	object_array = [];
	for image_filename in os.listdir(folder):
		print("[loadImages]: Loading image "+image_filename+"...");
		image_file = cv2.imread(folder+image_filename);

		if object_type is "plates":
			plateObject = Plate(image_file);
			object_array.append(plateObject);

		elif object_type is "classifier":
			classifierObject = Classifier(image_file);
			object_array.append(classifierObject);

	return object_array;

