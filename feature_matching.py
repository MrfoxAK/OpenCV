import cv2
import numpy as np

img1 = cv2.imread("C:\\Users\\AKASH\\OneDrive\\Desktop\\K2\\datasets\\x.jpg",cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("C:\\Users\\AKASH\\OneDrive\\Desktop\\K2\\datasets\\x3.jpg",cv2.IMREAD_GRAYSCALE)


# ORB detector
orb = cv2.ORB_create(nfeatures=1000)
kp1,des1 = orb.detectAndCompute(img1,None)
kp2,des2 = orb.detectAndCompute(img2,None)

# for d in des1:
#      print(d)

# Brute force matching
bf = cv2.BFMatcher()
matchs = bf.knnMatch(des1,des2,k=2)

# print(len(matchs))

# matchs = sorted(matchs,key=lambda x:x.distance)
# for m in matchs:
#      print(m.distance)
good=[]
for m,n in matchs:
     if m.distance < 0.85* n.distance:
          good.append([m])

print(len(good))
matching_res = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)



cv2.imshow("data",img1)
cv2.imshow("or",img2)
cv2.imshow("match",matching_res)
cv2.waitKey(0)
cv2.destroyAllWindows()













