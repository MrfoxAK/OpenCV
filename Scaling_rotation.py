# Scaling refers to the changing of height and weidth

import cv2
import numpy as np


img = cv2.imread("e.jpg")

# img_size = cv2.resize(img,(500,500))

# img_re_liner = cv2.resize(img,None,fx=5.5,fy=5.5,interpolation=cv2.INTER_LINEAR)
# img_re_cubic = cv2.resize(img,None,fx=5.5,fy=5.5,interpolation=cv2.INTER_CUBIC)

cv2.imshow("original",img)
# cv2.imshow("resize",img_size)
# cv2.imshow("liner",img_re_liner)
# cv2.imshow("cubic",img_re_cubic)

matrix = np.float32([[1,0,10],[1,0,10]])

# trans = cv2.warpAffine(img,matrix,(img.shape[1]+10,img.shape[0]+10))
# cv2.imshow("T",trans)

h,w = img.shape[:2]

matrix = cv2.getRotationMatrix2D((w/2,h/2),10,1)

trans = cv2.warpAffine(img,matrix,(w,h))

cv2.imshow("T",trans)

cv2.waitKey(0)






















