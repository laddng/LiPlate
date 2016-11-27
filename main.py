from modules.file_utils import *;
from modules.sift import *;
from modules.display_utils import *;
from modules.ocr_utils import *;
from modules.plates import *;

def run():

  images = loadImages("images/cars/");
  plates = locatePlates(images);
  plate_numbers = readPlates(plates);

  showResults(images, plates, plate_numbers);

  return True;

run();

