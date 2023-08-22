import cv2
import numpy as  np

#reading videos

capture=cv2.VideoCapture(r'C:\Users\Tejas\Downloads\dog.mp4')

while True:
    isTrue,frame=capture.read()
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could
    # not be read, or we're at the end of the video), we immediately
    # break from the loop.
    if isTrue:
        cv2.imshow('video',frame)
        if cv2.waitKey(0) & 0xFF==ord('d'):
            break
        else:
            break

capture.release()
cv2.destroyAllWindows()