import cv2 as cv

cam = cv.VideoCapture(0)

# Setting Resolution
def hd():
    cam.set(3, 1280)
    cam.set(4, 720)

def fhd():
    cam.set(3, 1920)
    cam.set(4, 1080)

hd()

# Writing the video to a file
frame_width = int(cam.get(3))
frame_height = int(cam.get(4))
out = cv.VideoWriter("D:/python/OpenCV/cam.mp4", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 60, (frame_width, frame_height))

while True:
    ret, frame = cam.read()
    if ret:
        out.write(frame)
        cv.imshow("webcam", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cam.release()
out.release()
cv.destroyAllWindows()
