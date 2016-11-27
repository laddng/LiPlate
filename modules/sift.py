import cv2;
import numpy as np;

def locatePlates(images):

  plates = [];

  for image in images:
    sift_result = sift(image);
    plate = cropSift(sift_result);
    plates.append(plate);

  return plates;

def sift(image):

  return sift_result;

def cropSift(sift_result):

  return plate;

