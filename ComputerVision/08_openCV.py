import cv2 as cv
import numpy as np
img = cv.imread("D:\python\OpenCV\me.jpg")
img = cv.resize(img,(600,600))
# horizontal side by side image
hor_img = np.hstack((img,img))
# verticle side by side image
ver_img = np.vstack((img,img))

ver_img=cv.resize(ver_img,(400,800))



cv.imshow("name",ver_img)
cv.waitKey(0)
cv.destroyAllWindows