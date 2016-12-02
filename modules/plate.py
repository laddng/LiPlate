import cv2;
import numpy as np;
from matplotlib import pyplot as plt;

class Plate:
	""" Class for the license plates """
	def __init__(self, image):
		self.original_image = image;
		self.plate_image = None;
		self.gray_image = None;
		self.plate_number = "None";
		self.roi = [];

	def grayImage(self):
		self.gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY);
		self.gray_image = cv2.GaussianBlur(self.gray_image, (29,29), 0);
		return True;

	def plateSearch(self):
		self.findContour();
		self.cropPlate();
		self.showResults();
		return True;

	def findContour(self):
		self.grayImage();

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
				cv2.rectangle(self.original_image, (x,y), (x+w, y+h), (0,255,0), 10);

		print("[findContour]: "+str(len(self.roi))+" potential plates found...");
		return True;

	def cropPlate(self):
		if len(self.roi) > 1:
			[x,y,w,h] = self.roi[0];
			self.plate_image = self.original_image[y:y+h,x:x+w];
		return True;

	def showResults(self):
		plt.figure();

		# original image
		plt.subplot(321);
		plt.imshow(self.original_image);
		plt.xlabel("Original image");

		# threshold image
		plt.subplot(322);
		plt.imshow(self.gray_image);
		plt.xlabel("Threshold image");

		# plate located
		plt.subplot(323);
		plt.imshow(self.original_image);
		plt.xlabel("Plate located");

		# plate cropped
		if self.plate_image is not None:
			plt.subplot(324);
			plt.imshow(self.plate_image);
			plt.xlabel("License plate #: "+str(self.plate_number));

		plt.show();
		return True;

