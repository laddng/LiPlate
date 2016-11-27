import cv2;
from sift import *;
from file_utils import *;

class Plate:

  def __init__(self):
    self.image = "";
    self.plate = "";
    self.plate_number = "";

  def loadImage(filename):
    self.image_filename = filename;
    self.image = cv2.imshow(filename);

  def findPlate():
    self.plate = findPlate(self.image);

  def readPlate():
    self.plate_number = readPlate(self.plate);

