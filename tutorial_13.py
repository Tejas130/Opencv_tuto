import cv2
import numpy as np

img=cv2.imread(r'C:\Users\Tejas\Downloads\park.jpg')
cv2.imshow('park_img',img)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_img',gray_img)

#laplacian gradients

laplacian_grad=cv2.Laplacian(gray_img,cv2.CV_64F)
lap = np.uint8(np.absolute(laplacian_grad))
cv2.imshow('Laplacian', lap)

#sobel gradients
sobelx=cv2.Sobel(gray_img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1)
combined_sobel = cv2.bitwise_or(sobelx, sobely)

cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Combined Sobel', combined_sobel)

canny=cv2.Canny(gray_img,150,175)
cv2.imshow('canny_img',canny)
cv2.waitKey(0)