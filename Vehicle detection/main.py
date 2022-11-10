import cv2


cap = cv2.VideoCapture(
    "C:\\Users\\AKASH\\OneDrive\\Desktop\\Vehicle detection\\carv3.avi")

car_cascade = cv2.CascadeClassifier(
    "C:\\Users\\AKASH\\OneDrive\\Desktop\\Vehicle detection\\carx.xml")


while True:

     ret, frame = cap.read()

     gray_s = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     cars = car_cascade.detectMultiScale(gray_s, 1.1, 2)

     # print(cars)

     for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
     cv2.imshow('video', frame )
     if cv2.waitKey(33) == 27:
          break


cv2.destroyAllWindows()
















