import numpy as np
import cv2 as cv
from cv2 import cvtColor
# Reading image
img = cv.imread("D:/python/OpenCV/me.jpg")
# resize image
img = cv.resize(img,(800,600))

# gray conversion
gray = cvtColor(img,cv.COLOR_BGRA2GRAY)


cv.imshow("First Image", img)
cv.imshow("second Image", gray)
# for delay in image 
cv.waitKey(0)
cv.destroyAllWindows()
