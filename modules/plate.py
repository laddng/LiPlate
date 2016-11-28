import cv2;
import numpy as np;

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
		key1, des1 = sift.detectAndCompute(self.gray_image);
		key2, des2 = sift.detectAndCompute(training_image);

		MIN_MATCH_COUNT = 10;
		FLANN_INDEX_KDTREE = 0;

		index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5);
		search_params = dict(checks = 50);

		flann = cv2.FlannBasedMatcher(index_params, search_params);

		matches = flann.knnMatch(des1, des2, k=2);

		# store all good matches
		good_matches = [];
		for m,n in matches:
			if m.distance < 0.7*n.distance:
				good_matches.append(m);

		# if there are enough matches
		if len(good) > MIN_MATCH_COUNT:
			src_pts = np.float32([ key1[ m.queryIdx ].pt for m in good]).reshape(-1,1,2);
			dst_pts = np.float32([ key2[ m.trainIdx ].pt for m in good]).reshape(-1,1,2);
			M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0);

			height, width = self.original_image;
			pts = np.float32([[0,0],[0,height-1],[width-1, height-1],[width-1, 0]]).reshape(-1,1,2);
			dst = cvs.perspectiveTransform(pts, M);

			training_image = cv2.polylines(self.original_image, [np.int32(dst)], True, 255,3, cv2.LINE_AA);

		else:
			print("Not enough matches found for this image.");
			matchesMask = None;

		draw_params = dict(matchColor = (0,255,0),
					singlePointcolor = None,
					matchesMask = matchesMask,
					flags = 2 );

		final_image = cv2.drawMatches(self.original_image, key1, training_image, key_2, good, None, **draw_params);
		
		plt.imshow(final_image, 'gray'), plt.show();
		return True;

	def readPlate(self):
		return True;

