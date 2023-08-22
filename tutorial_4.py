import cv2
import numpy as np
 #read an image
park_img=cv2.imread(r'C:\Users\Tejas\Downloads\park.jpg')
cv2.imshow('imgage',park_img)

# #converting grayscale
# gray=cv2.cvtColor(park_img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray_img',gray)
#
# #blur
# gauss=cv2.GaussianBlur(park_img,(7,7),cv2.BORDER_DEFAULT)
# cv2.imshow('blur_img',gauss)
#
# #Edge cascade
# cascade=cv2.Canny(gauss,125,175)
# cv2.imshow('cascade_img',cascade)
# #dialted image
# dila=cv2.dilate(cascade,(7,7),iterations=3)
# cv2.imshow('dilate_img',dila)
#
# #erode image
# erode=cv2.erode(dila,(7,7),iterations=3)
# cv2.imshow('erode_img',erode)

#resize image
resize=cv2.resize(park_img,(500,500),interpolation=cv2.INTER_LINEAR)
cv2.imshow('resize_img',resize)

#cropping
crop=park_img[50:200,200:400]
cv2.imshow('crop_img',crop)

cv2.waitKey(0)
cv2.destroyAllWindows()

