import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("C:\\Users\\AKASH\\OneDrive\\Desktop\\K2\\datasets\\coins.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



blur = cv2.GaussianBlur(gray, (11,11),0)


canny = cv2.Canny(blur, 30, 150, 3)

dilated = cv2.dilate(canny, (1,1), iterations=2)

cv2.imshow('d',dilated)
cv2.waitKey(0)

(cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print(len(cnt))


