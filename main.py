from modules.file_utils import *;
from modules.plate import *;

def run():

	plates_array = loadImages("images/cars/");
	print("[run]: All images have been downloaded.");

	print("[run]: Starting contour search for plate shapes...");
	for plate in plates_array:
		plate.findContour();

	return True;

run();

