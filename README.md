# LiPlate

This Python/OpenCV script takes a series of images of cars and determines where their license plates are. Afterwards, it attempts to read the plate number and display it to the user.

Inputs: Images of cars.

Outputs: Cropped images of license plates, clearly showing their numbers.

Constraints: Only front or back photos of cars in clear daylight.

Assumptions: License plates are USA plates with 6-8 characters in the plate number.

## Setup
Make sure to have the latest version of Python installed on your local machine. In addition, install OpenCV for Python to execute the image analysis functions. The Tesseract library is needed for the Tesseract-OCR version of this program as well.

Once the dependencies are installed, run the program by simply placing your images inside `/images` and execute:

```
$ python main.py
```

Dependencies:

* pytesseract

* PIL/python-pillow

* OpenCV

* matplotlib

* tesseract

* tesseract-data-eng library

## Initial Approach - SIFT Algorithm
Initially, I attempted to solve this problem using the SIFT algorithm. With the training image being an image of a license plate, I looped through all the photos of cars and tried to identify similar features with OpenCV's SIFT function. This proved unsuccessful because there was not enough similarity between the one training image I was using and the different images of cars who had different plate numbers as well as plate colors. In addition, there was too much noise in my testing images of cars. An attempt to remove the noise with a heavy Gaussian Blur did not work as well.

SIFT is a great algorithm if you are sure that your training image is very similar to your test image in terms of features and edges. However, if you are just looking for similarity, it can be difficult to perfect.

## Successful Approach - Contours Algorithm
After failing to identify the license plates with the SIFT algorithm and a training image, I moved on to use an algorithm that looked for contours similar to the shape of a license plate. The algorithm is described below:

### Step 1: Thresholding
Firstly, the image is converted to grayscale using OpenCV's cvtColor function. Then I used thresholding on the image of the car to really bring out the contour of the license plate in the image of the car. The tricky part is finding the right threshold value that will successfully bring out the plate.

### Step 2: Filtering Contours
After thresholding the image, I searched for contours within the image. The contour had to match rougly the shape of a rectangle that was around 150px wide and 80px high (average image dimensions of the license plates in all the testing images). If the contour matched that size range, it was considered the license plate. If there were multiple matches, I just took the first one. Given more time, I would use a better approach to search through the multiple matches to find the best contour that could be a plate.

### Step 3: Region of Interest
With our license plate contour identified, I drew a green rectangle around it using OpenCV's rectangle function to indicate that we have found a contour that matches a plate dimension. We now have a new region of interest (ROI) for analysis. The image was cropped to just show our ROI so that we can begin to read the plate numbers.

### Step 4: Finding Plate Numbers
Using the method of contours again, I found all the contours in our new ROI and selected those that roughly matched the dimensions of a character in a license plate. I appended a cropped image of each contour found to an array. This array is a series of images of characters that I would like to read.

### Step 5: Reading Characters
Now that I have done all the work to narrow down our search from car to plate to character, I want to convert that image to an actual character that I can record and add to our guessed plate number.

I tried two approches to this problem. Firstly, I created 35 images of characters A-Z, 1-9 in a font that matched many of the fonts used in license plates. I imported all those images and ran a SIFT comparison between the training image character that I created and the character I found in the plate. The best match was declared at the end of the loop, and that be came the guess of my character in the license plate. This DIY approach had minor success in reading the plate characters.

The second approach was to use HP/Google's Tesseract Optical Character Recognition open source library. With this library, you simply provide an image and the Tesseract library attempts to return a string with what it thinks is the text. I was able to have a lot more success reading the plate characters this way.

## Summary
In all, I approached this problem from many different directions. There is actually a lot of research done on ALPR systems (Automatic License Plate Recognition systems) since there are many applications for these programs.

Working through SIFT, contours, and OCR was extremely fascinating since each had its strengths and weaknesses when contributing results to the problem at hand.

## Versions
There were many different approaches mentioned above in my research. I took care to create different Git branches for each approach so that you can try the different ways I approached this problem. Branches:

	* `master` : Contains the best version of this program.

	* `SIFT-method`: The original approach I had to the problem using the SIFT algorithm.

	* `SIFT-OCR`: Attempts to read the characters in the plate using the SIFT algorithm and a predefined series of images of license plate characters

	* `Tesseract-OCR`: Attempts to read the characters in the plate using the Tesseract OCR library developed by HP/Google

### License
This is an academic project for a CS class at Wake Forest University. It is purely for academic use and is licensed under the MIT license.

### Credits
Code by Niclas Ladd - WFU '16. Class: CSC 391-Computer Vision by Dr. Li and Dr. Pauca of Wake Forest University.

