# Required modules
import cv2
import numpy as np
import matplotlib.pyplot as plt

min_YCrCb = np.array([0,133,77],np.uint8)
max_YCrCb = np.array([235,173,127],np.uint8)

# Get pointer to video frames from primary device
image = cv2.imread("test.jpg")
imageYCrCb = cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB)
skinRegionYCrCb = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)

skinYCrCb = cv2.bitwise_and(image, image, mask = skinRegionYCrCb)

cv2.imwrite("test.jpg", np.hstack([image,skinYCrCb]))

def convolve(B, r):
    D = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(r,r))
    cv2.filter2D(B, -1, D, B)
    return B

#Loading the image and converting to HSV
image = cv2.imread('test.jpg')
image_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
model_hsv = image_hsv[225:275,625:675] # Select ROI

#Get the model histogram M
M = cv2.calcHist([model_hsv], channels=[0, 1], mask=None,
                  histSize=[80, 256], ranges=[0, 180, 0, 256] )

#Backprojection of our original image using the model histogram M
B = cv2.calcBackProject([image_hsv], channels=[0,1], hist=M,
                         ranges=[0,180,0,256], scale=1)

B = convolve(B, r=5)

#Threshold to clean the image and merging to three-channels
_, thresh = cv2.threshold(B, 30, 255, cv2.THRESH_BINARY)
cv2.imwrite("test1.jpg",cv2.cvtColor(model_hsv,cv2.COLOR_HSV2RGB))
cv2.imwrite("test1.jpg",cv2.bitwise_and(image,image, mask = thresh))

