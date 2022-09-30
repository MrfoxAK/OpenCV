import cv2
from cv2 import waitKey
import face_recognition as fr
from time import sleep
from simple_facerec import SimpleFacerec

# img = cv2.imread("C:\\Users\\AKASH\\OneDrive\\Desktop\\K2\\source code\\Messi1.webp")
# rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# img_encoding = fr.face_encodings(rgb_img)[0]


# img1 = cv2.imread("C:\\Users\\AKASH\\OneDrive\\Desktop\\K2\\messi.jpg")
# rgb_img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
# img_encoding1 = fr.face_encodings(rgb_img1)[0]


# result = fr.compare_faces([img_encoding],img_encoding1)


# print("Result: ",result)


# cv2.imshow("messi",img)
# cv2.imshow("Elon",img1)
# cv2,waitKey(0)

sfr = SimpleFacerec()
sfr.load_encoding_images("C:\\Users\\AKASH\\OneDrive\\Desktop\\K2\\source code\\images")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # detect faces
    face_locations,face_names = sfr.detect_known_faces(frame)
    for face_loc,name in zip(face_locations,face_names):
        # print(face_loc)
        y1,x1,y2,x2 = face_loc[0],face_loc[1],face_loc[2],face_loc[3]
        cv2.putText(frame,name,(x1,y1-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,200),2)
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,200),2)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


# import cv2

# videoCaptureObject = cv2.VideoCapture(0)
# result = True
# while(result):
#     ret,frame = videoCaptureObject.read()
#     cv2.imshow("Frame",frame)
#     sleep(15)
#     cv2.imwrite("myFace.jpg",frame)
#     result = False
# videoCaptureObject.release()
# cv2.destroyAllWindows()
