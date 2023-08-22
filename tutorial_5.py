import cv2
import numpy as np

#read img
cat_img=cv2.imread(r'C:\Users\Tejas\Downloads\cats 2.jpg')
cv2.imshow('cats',cat_img)

blank=np.zeros(cat_img.shape,dtype='uint8')
cv2.imshow('bank_img',blank)

# gray=cv2.cvtColor(cat_img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray_img',gray)

# Gauss=cv2.GaussianBlur(cat_img,(7,7),cv2.BORDER_DEFAULT)
# cv2.imshow('gauss_img',Gauss)
#
# ret,thresh_binary=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
# cv2.imshow('binary_img',thresh_binary)

canny=cv2.Canny(cat_img,125,255)
cv2.imshow('canny_img',canny)

cont,hierchies=cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(cont)} contour(s) found!')

#draw countour img
cv2.drawContours(blank,cont,-1,(0,0,255),1)
cv2.imshow('Contours Drawn', blank)
cv2.waitKey(0)
