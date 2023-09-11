# how to draw lines and shapes in Python

import cv2 as cv
import numpy as np

img = np.zeros((500,500))
# adding colour in canvas
coloured_img = np.zeros((500,500,3),np.uint8)
coloured_img[:] = 105,0,1
coloured_img[100:150,300:400] = 105,0,255

# Adding the line into canvas
cv.line(coloured_img,(0,0),(300,600),(255,0,340),3)

#Adding rectangular
cv.rectangle(coloured_img,(50,100),(300,400),(255,0,340),3)
cv.rectangle(coloured_img,(50,100),(300,400),(255,0,340),cv.FILLED)

# Adding the circle
cv.circle(coloured_img,(400,300),50,(255,8,440),3)
cv.circle(coloured_img,(400,300),50,(255,8,440),cv.FILLED)

# Adding the text 
cv.putText(coloured_img,"Sheryyy",(170,30),cv.FONT_HERSHEY_COMPLEX,1,(255,8,440),1)



cv.imshow("image",coloured_img)
cv.waitKey(0)
cv.destroyAllWindows()