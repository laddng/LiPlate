from modules.file_utils import *;
from modules.plate import *;

def run():

	plates_array = loadImages("images/cars/");
	training_image = cv2.imread("images/training_image.jpg");
	training_image = cv2.cvtColor(training_image, cv2.COLOR_BGR2GRAY);

	print("[run]: All images have been downloaded.");

	print("[run]: Starting SIFT search for images...");

	for plate in plates_array:
		plate.findPlate(training_image);

	print("[run]: SIFT search ended. End of program.");

	return True;

run();

