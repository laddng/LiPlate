import cv2;
import numpy as np;
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
		# apply a heavy gaussian blur
		self.gray_image = cv2.GaussianBlur(self.gray_image, (45,45), 0);

	def findContour(self):
		self.grayImage();
		ret, threshold = cv2.threshold(self.gray_image, 127, 255, 0);
		image, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE);
		potential_plates = [];
		w = 0;

		print("[findContour]: "+str(len(contours))+" contours found...");

		for contour in contours:
			area = cv2.contourArea(contour);
			if area > 200 and area < 400:
				[w,h,x,y] = cv2.boundingRect(contour);

			if w > 50:
				potential_plates.append(contour);
				cv2.fillPoly(self.original_image, pts=contour, color=(255,255,255));

		#final_image = cv2.drawContours(self.original_image, potential_plates, -1, (0,255,0), 4);

		plt.figure();
		plt.imshow(final_image);
		plt.show();

