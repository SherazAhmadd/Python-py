# How to change the perspective of image
import cv2 as cv
import numpy as np

def find_cord(event, x, y, flags, param):
    if event == cv.EVENT_FLAG_LBUTTON:  # Use cv.EVENT_LBUTTONDOWN for left mouse button click
        print(x, y)
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x) + ',' + str(y), (x, y), font, 1, (255, 0, 0), thickness=2)
        cv.imshow("image", img)

if __name__ == "__main__":  # Correct the condition
    img = cv.imread("D:/python/OpenCV/warp.png")
    cv.imshow("image", img)
    cv.setMouseCallback("image", find_cord)  # Correct window name to "image"
   
# ------------------------------------------------
# # defining the points
p1 = np.float32([[128,51],[302,52],[358 ,248],[72 ,249]])
width = 389
height = 296

p2 = np.float32([[0,0],[389,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(p1,p2)
out_img = cv.warpPerspective(img,matrix,(width,height))
cv.imshow("transform",out_img)
cv.waitKey(0)
cv.destroyAllWindows()
