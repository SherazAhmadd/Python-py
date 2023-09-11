# Functions and manipulation of image
import numpy as np
import cv2 as cv
img = cv.imread("D:\python\OpenCV\me.jpg")
# resized
r_img = cv.resize(img,(400,400))
# blurr
blur = cv.GaussianBlur(r_img,(23,23),0)
# edge detection
e_img = cv.Canny(r_img,48,45)
# for Dilation
kernal_matix = np.ones((3,3),np.uint8) # for extra dilation on edges
dilated_img = cv.dilate(e_img,(7,7),iterations=1) # for thick the edges
# for thinning the edges
ero_img = cv.erode(e_img,(7,7),iterations=1)
# for Crop the image 
print("the height n width of image",r_img.shape)
croped_image = r_img[50:170,120:250]
print("the height n width of croped image",croped_image.shape)


# cv.imshow("image",img)
cv.imshow("img",r_img)
# cv.imshow("imge",blur)
# cv.imshow("edge detected image",e_img)
# cv.imshow("Dilated",dilated_img)
# cv.imshow("Erossion ",ero_img)
cv.imshow("croped ",croped_image)
cv.waitKey(0)
cv.destroyAllWindows()
