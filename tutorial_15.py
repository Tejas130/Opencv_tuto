import cv2
import  numpy as np
img=cv2.imread(r'C:\Users\Tejas\Downloads\park.jpg')
cv2.imshow('park',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow('balnk_img',blank)

circle=cv2.circle(blank.copy(),(img.shape[1]//2+45,img.shape[0]//2),100,255,-1)
rectangle=cv2.rectangle(blank.copy(),(30,30),(370,370),255,-1)

weird_shape=cv2.bitwise_and(circle,rectangle)
cv2.imshow('weird_shape',weird_shape)


#mask
mask=cv2.bitwise_and(img,img,mask=weird_shape)
cv2.imshow('mask_img',mask)
cv2.waitKey(0)