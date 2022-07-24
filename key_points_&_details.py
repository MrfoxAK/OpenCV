import cv2
import numpy as np

img =  cv2.imread('test.jpg',0)

orb = cv2.ORB_create(100)

kp, des = orb.detectAndCompute(img,None)

img2 = cv2.drawKeypoints(img,kp,None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("original",img)
cv2.imshow("ORB",img2)

cv2.waitKey(0)










