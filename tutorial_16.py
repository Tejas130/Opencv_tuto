import cv2
import numpy as np

img=cv2.imread(r'C:\Users\Tejas\Downloads\park.jpg')
cv2.imshow('park_img',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow('blank_img',blank)

cv2.waitKey(0)

#split img
b,g,r=cv2.split(img)

blue=cv2.merge([b,blank,blank])
green=cv2.merge([blank,g,blank])
red=cv2.merge([blank,blank,r])

cv2.imshow('blue',blue)
cv2.imshow('green',green)
cv2.imshow('red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merge all img
bgr_img=cv2.merge([b,g,r])
cv2.imshow('merged',bgr_img)



cv2.waitKey(0)
