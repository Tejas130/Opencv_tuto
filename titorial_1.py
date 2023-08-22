import os
import cv2
import numpy as np

#get images froma video????
#if you want create numpy array and save it as img file using imwrite function

path=r'C:\Users\Tejas\Desktop\WEB APP.mp4'
os.mkdir("video_to_imag") # create directory to save img
cap=cv2.VideoCapture(path)

img_count=1
while cap.isOpened():
    _,frame=cap.read()

    if not _:
        print("unable to read")
        break
    is_img_write=cv2.imwrite(f"video_to_imag\image{img_count}.jpeg",frame)

    if is_img_write:
        print(f"save iamge ast video_to_imag\image{img_count}.jpeg")

    cv2.imshow('video',frame)
    cv2.waitKey(25) & 0xff == ord('q')
    img_count=img_count+1
cap.release()
cv2.destroyAllWindows()


