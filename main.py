from modules.file_utils import *;
from modules.plate import *;

def run():

	plates_array = loadImages("images/cars/");
	print("[run]: All testing images have been downloaded.");

	for plate in plates_array:
		plate.plateSearch();

	print("[run]: Finished plate recognition.");
	return True;

run();

