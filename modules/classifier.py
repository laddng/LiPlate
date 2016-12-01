import cv2;
import numpy as np;
import sys;
import string;

class Classifier:
	""" License plate character classifier """
	training_responses = [];
	training_samples = [];

	def __init__(self, image):
		self.original_image = image;

	def grayImage(self):
		self.gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY);

	def OCRTrain(self):
		self.grayImage();
		blur = cv2.GaussianBlur(self.gray_image, (5,5), 0);
		threshold = cv2.adaptiveThreshold(blur, 255, 1,1,11,2);

		_,contours,hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE);

		samples = np.empty((0,100));
		responses = [];
		keys = [i for i in range(0, 2000)];
		h = 0;

		for contour in contours:
			if cv2.contourArea(contour) > 100:
				[x,y,w,h] = cv2.boundingRect(contour);

			if h > 28:
				cv2.rectangle(self.gray_image, (x,y), (x+w, y+h),(0,0,255), 2);
				roi = threshold[y:y+h, x:x+w];
				roismall = cv2.resize(roi, (10,10));
				cv2.imshow("Training Image", self.gray_image);
				key = cv2.waitKey(0);

				if key == 27:
					sys.exit();
				elif key in keys:
					print("[OCRTrain]: Character recorded: "+str(chr(key)));
					responses.append(int(chr(key)));
					sample = roismall.reshape((1,100));
					samples = np.append(samples, sample, 0);
		responses = np.array(responses, np.float32);
		responses = responses.reshape((responses.size, 1));

		self.training_responses.append(responses);
		self.training_samples.append(samples);

