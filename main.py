import cv2
import numpy as np

original = cv2.imread("test.jpg")
duplicate = cv2.imread("dub.jpg")

# 1st check if 2 are equals or not
image1 = original.shape
image2 = duplicate.shape
# print(image1)
# print(image2)
if original.shape == duplicate.shape:
    print("the images have same size")
    dif = cv2.subtract(original,duplicate)
    cv2.imshow("dif",dif)
    b,g,r = cv2.split(dif)
    # cv2.imshow("b",b)
    # cv2.imshow("g",g)
    # cv2.imshow("r",r)
    print(cv2.countNonZero(b))
    if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
        print("the images are same")


cv2.imshow("original",original)
cv2.imshow("duplicate",duplicate)
cv2.waitKey(0)
cv2.destroyAllWindows()