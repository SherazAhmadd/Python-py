# using open Cv colorfull to black n white
import cv2 as cv
from cv2 import cvtColor

img = cv.imread("D:/python/OpenCV/me.jpg")
img = cv.resize(img,(600,600))
grey = cvtColor(img,cv.COLOR_BGR2GRAY)
# changing image into Black n White
(thresh,b_w) = cv.threshold(grey,127,155,cv.THRESH_BINARY)
# saving the image into local file
cv.imwrite("D:/python/OpenCV/me_gray.jpg",grey)

cv.imshow("first",img)
cv.imshow("2nd",grey)
cv.imshow("black and white",b_w)
cv.waitKey(0)