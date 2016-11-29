import cv2;
import numpy as np;
from modules.classifier import *;
from matplotlib import pyplot as plt;

class Plate:
	""" A class for the license plates """
	def __init__(self, image):
		self.original_image = image;
		self.plate_image = None;
		self.gray_image = None;
		self.plate_number = "";

	def grayImage(self):
		self.gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY);

	def findPlate(self, classifiers):
		model = cv2.ml.KNearest_create();
		return True;

