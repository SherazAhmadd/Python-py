import cv2 as cv 

vid = cv.VideoCapture("D:/python/OpenCV/nice.mp4")
if(vid.isOpened() == False):
    print("Error in video uploading")

# reading and playing
# while(vid.isOpened()):
#     ret, frame = vid.read()
#     if ret == True:
#         cv.imshow("video",frame)
#         if cv.waitKey(1) & 0xFF == ord("q"):
#             break
#     else: 
#         break

#------------------------------------------------------------------------------

# saving the video
# 1--> write the format 2--> codec 3 --> video writer object and file output
frame_width = int(vid.get(3))
frame_height = int(vid.get(4))
out = cv.VideoWriter("output.mp4",cv.VideoWriter_fourcc("M","J","P","G"),10,(frame_width,frame_height),isColor=False)

# converting into Gray video
while(True):
    ret,frame1 = vid.read()
    grayvid = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
    if ret == True:
        out.write(grayvid)
        cv.imshow("video_gray",grayvid)
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
vid.release()
out.release()
cv.destroyAllWindows()