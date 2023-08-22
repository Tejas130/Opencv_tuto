import cv2
import numpy as np
#play video???
path=r'C:\Users\Tejas\Desktop\WEB APP.mp4'
cap=cv2.VideoCapture(path)
while cap.isOpened():
    _,frame=cap.read()
    if _:
        img_size=cv2.resize(frame,(600,400))
        cv2.imshow('video',img_size)

        if cv2.waitKey(25) & 0xff == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
#you can show 4 videos in one window also different videos in one window just used different frame