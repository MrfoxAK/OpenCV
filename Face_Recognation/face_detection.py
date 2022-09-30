import cv2
from cv2 import waitKey
import face_recognition as fr

img = cv2.imread("C:\\Users\\AKASH\\OneDrive\\Desktop\\K2\\source code\\Messi1.webp")
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_encoding = fr.face_encodings(rgb_img)[0]


img1 = cv2.imread("C:\\Users\\AKASH\\OneDrive\\Desktop\\K2\\messi.jpg")
rgb_img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img_encoding1 = fr.face_encodings(rgb_img1)[0]


result = fr.compare_faces([img_encoding],img_encoding1)


print("Result: ",result)


cv2.imshow("messi",img)
cv2.imshow("Elon",img1)
cv2,waitKey(0)


















