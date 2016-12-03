import cv2;
import numpy as np;
from matplotlib import pyplot as plt;
from copy import deepcopy, copy;
import logging;
from logging.config import fileConfig;

fileConfig("logging_config.ini");
logger = logging.getLogger();

class Plate:
	""" Class for the license plates """
	def __init__(self, image):				### Plate Class Vars ###
		self.original_image = image;			# original image of analysis
		self.plate_located_image = deepcopy(image);	# original image with plate hilighted
		self.plate_image = None;			# license plate cropped
		self.plate_image_char = None;			# license plate cropped, chars outlined
		self.gray_image = None;				# original image - grayscale for analysis
		self.plate_number = "None found.";		# plate number
		self.roi = [];					# regions of interest for plates
		logger.info("New plate created.");

	def grayImage(self, image):
		logger.info("Image converted to grayscale");
		return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);

	def plateSearch(self):
		self.findContour();
		self.cropPlate();
		if self.plate_image is not None:
			self.readPlateNumber();
		self.showResults();
		return True;

	def findContour(self):
		self.gray_image = self.grayImage(deepcopy(self.original_image));
		self.gray_image = cv2.GaussianBlur(self.gray_image, (29,29), 0);

		ret, threshold = cv2.threshold(self.gray_image, 127, 255, 0);
		_,contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE);

		w,h,x,y = 0,0,0,0;

		for contour in contours:
			area = cv2.contourArea(contour);

			# rough range of areas of a license plate
			if area > 6000 and area < 40000:
				[x,y,w,h] = cv2.boundingRect(contour);

			# rough dimensions of a license plate
			if w > 100 and w < 200 and h > 60 and h < 100:
				self.roi.append([x,y,w,h]);
				cv2.rectangle(self.plate_located_image, (x,y), (x+w, y+h), (0,255,0), 10);

		logger.info("%s potential plates found.", str(len(self.roi)));
		return True;

	def cropPlate(self):
		if len(self.roi) > 1:
			[x,y,w,h] = self.roi[0];
			self.plate_image = self.original_image[y:y+h,x:x+w];
			self.plate_image_char = deepcopy(self.plate_image);
		return True;

	def readPlateNumber(self):
		self.plate_number = "License plate #: None found";
		self.findCharacterContour();
		return True;

	def findCharacterContour(self):
		gray_plate = self.grayImage(deepcopy(self.plate_image));
		gray_plate = cv2.GaussianBlur(gray_plate, (5,5), 0);

		_,threshold = cv2.threshold(gray_plate, 127, 255, 0);
		_,contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE);

		character_roi = [];
		w,h,x,y = 0,0,0,0;

		logger.info("%s contours found.", str(len(contours)));
		for contour in contours:
			area = cv2.contourArea(contour);

			# rough range of areas of a plate number
			if area > 120 and area < 2000:
				[x,y,w,h] = cv2.boundingRect(contour);

			# rough dimensions of a character
			if h > 20 and h < 90 and w > 10 and w < 50:
				character_roi.append([x,y,w,h]);
				cv2.rectangle(self.plate_image_char, (x,y), (x+w, y+h), (0,0,255), 1);

		logger.info("Plate characters found");
		return True;

	# we will have a catalogue of every character and number
	# A-Z, 1-9 where we will compare the histogram to the 
	# plate character and the highest score will be the correct
	# plate character
	def histogramComparison(self):
		return True;

	def plot(self, figure, subplot, image, title):
		figure.subplot(subplot);
		figure.imshow(image);
		figure.xlabel(title);
		figure.xticks([]);
		figure.yticks([]);
		return True;

	def showResults(self):
		plt.figure(self.plate_number);

		self.plot(plt, 321, self.original_image, "Original image");
		self.plot(plt, 322, self.gray_image, "Threshold image");
		self.plot(plt, 323, self.plate_located_image, "Plate located");

		if self.plate_image is not None:
			self.plot(plt, 324, self.plate_image, "License plate");
			self.plot(plt, 325, self.plate_image_char, "Characters outlined");

		plt.tight_layout();
		plt.show();
		return True;

