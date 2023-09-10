import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) # 0 indicates webcam number
# setting the camera
cap.set(10,100) # 10 for brightness
cap.set(3,1080) # 3 for width
cap.set(4,1280) # 4 for height
if(cap.isOpened()==False):
    print("There is an error")

width = int(cap.get(3))
height = int(cap.get(4))
output = cv.VideoWriter("D:/python/OpenCV/web_out3.mp4",cv.VideoWriter_fourcc("M","J","P","G"),10,(width,height))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        output.write(frame)
        cv.imshow("webcam",frame)
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
output.release()
cv.destroyAllWindows()