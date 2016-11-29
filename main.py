from modules.file_utils import *;
from modules.plate import *;

def run():
	print("[run]: Downloading images...");
	plates_array = loadImages("images/cars/", "plates");
	classifier_array = loadImages("images/classifiers/", "classifier");
	print("[run]: All images have been downloaded.");

	print("[run]: Training OCR classifiers...");
	for classifier in classifier_array:
		classifier.OCRTrain();
	print("[run]: Finished training OCR classifiers...");

	print("[run]: Finding plates in car images...");
	for plate in plates_array:
		plate.findPlate(Classifier.training_responses);
	print("[run]: Finished searching for plates in car images...");

	return True;

run();

