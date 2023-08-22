import cv2
import numpy as np

img=cv2.imread(r'C:\Users\Tejas\Downloads\park.jpg')
cv2.imshow('park_img',img)

#colourspaces
# #bgr to grayscale
gary_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_img',gary_img)
#
# ## BGR to HSV
# hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv_img',hsv_img)
#
# #HSV to BGR
# bgr_img=cv2.cvtColor(hsv_img,cv2.COLOR_HSV2BGR)
# cv2.imshow('bgr_img',bgr_img)
# #BGR to L*A*B
# Lab_img=cv2.cvtColor(bgr_img,cv2.COLOR_BGR2LAB)
# cv2.imshow('lab_img',Lab_img)
#
# #BGR to RGB
# RGB_img=cv2.cvtColor(bgr_img,cv2.COLOR_BGR2RGB)
# cv2.imshow('rgb_img',RGB_img)

#gray to rgb
rgb_gray=cv2.cvtColor(gary_img,cv2.COLOR_GRAY2RGB)
cv2.imshow('rgb_gray',rgb_gray)

cv2.waitKey(0)

