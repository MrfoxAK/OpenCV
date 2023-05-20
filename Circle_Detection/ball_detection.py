import cv2 as cv
import numpy as np



vc = cv.VideoCapture(0)
prevCircle = None
dist = lambda x1,y1,x2,y2: (x1-x2)**2+(y1-y2)**2

while True:

     ret, frame = vc.read()
     if not ret:
          break

     grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
     blurFrame = cv.GaussianBlur(grayFrame,(17,17),0)

     circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=75,maxRadius=400)
     # distance btwn 2 circle is 100
     # param1 stands for the sensitivity to detect the circle 
     # param2 is the min no.of edges around the circle tp detect it is a circle

     if circles is not None:
          circles = np.uint16(np.around(circles))
          choosen = None
          for i in circles[0, :1]:
               if choosen is None:
                    choosen = i
               if prevCircle is not None:
                    if dist(choosen[0],choosen[1],prevCircle[0],prevCircle[1] <= dist(i[0],i[1],prevCircle[0],prevCircle[1])):
                         choosen = i
          cv.circle(frame,(choosen[0],choosen[1]), 1,(0,100,100),3)
          cv.circle(frame,(choosen[0],choosen[1]),choosen[2],(0,100,100),3)
          prevCircle = choosen


     cv.imshow("frame",frame)
     if cv.waitKey(1) & 0xFF == ord('q'):
          break

vc.release()
cv.destroyAllWindows()















