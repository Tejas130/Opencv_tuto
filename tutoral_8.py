import cv2
import numpy as np

img=cv2.imread(r'C:\Users\Tejas\Downloads\cats.jpg')
cv2.imshow('img',img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

#simple thresholding
threshold,thresh=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
cv2.imshow('thresh_img',thresh)

threshold,thresh_inv=cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
cv2.imshow('thresh_img',thresh_inv)

#adaptive thresholding
adaptive_thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,9)
cv2.imshow('thresh_ad_img',adaptive_thresh)
cv2.waitKey(0)