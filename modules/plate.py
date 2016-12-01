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

	def findPlate(self, training_image):
		self.grayImage();

		sift = cv2.xfeatures2d.SIFT_create();

		# find keypoints
		key1, des1 = sift.detectAndCompute(self.gray_image, None);
		key2, des2 = sift.detectAndCompute(training_image, None);

		# BFMatcher
		bf = cv2.BFMatcher();
		matches = bf.knnMatch(des1, des2, k=2);

		good = [];
		for m,n in matches:
			if m.distance < 0.6*n.distance:
				good.append([m]);

		final_image = self.gray_image;
		final_image = cv2.drawMatchesKnn(self.gray_image, key1, training_image, key2, good, final_image, flags=2);

		print("[findPlate]: Finished analysis, showing results...");

		plt.imshow(final_image, 'gray'), plt.show();
		return True;

	def readPlate(self):
		return True;

