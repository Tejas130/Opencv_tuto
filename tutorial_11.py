import cv2
import numpy as np

img=cv2.imread(r'C:\Users\Tejas\Downloads\cats.jpg')
cv2.imshow('cats_img',img)

#averaging blurr
avg_img=cv2.blur(img,(3,3))
cv2.imshow('Average Blur', avg_img)

#gaussian blur
gauss_blur=cv2.GaussianBlur(img,(3,3),0)
cv2.imshow('gauss_img',gauss_blur)

#median blur
med_blur=cv2.medianBlur(img,3)
cv2.imshow('med_img',med_blur)
#bilateral
bil_img=cv2.bilateralFilter(img,10,35,25)
cv2.imshow('bil_img',bil_img)

cv2.waitKey(0)