import cv2
import numpy as np

img=cv2.imread(r'C:\Users\Tejas\Downloads\park.jpg')
cv2.imshow('img_park',img)

#translation
# def translate(img,x,y):
#     tranlation_matrix=np.float32([[1,0,x],[0,1,y]])
#     dimensions=(img.shape[1],img.shape[0])
#     return cv2.warpAffine(img,tranlation_matrix,dimensions)
# # -x --> Left
# # -y --> Up
# # x --> Right
# # y --> Down
#
# translated=translate(img,-100,100)
# cv2.imshow('trans_img',translated)


#rotaion
# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]
#
#     if rotPoint is None:
#         rotPoint = (width // 2, height // 2)
#
#     rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)
#
#     return cv2.warpAffine(img, rotMat, dimensions)
#
# rotated = rotate(img, -45)
# cv2.imshow('Rotated', rotated)
#
# rotated_rotated = rotate(img, -90)
# cv2.imshow('Rotated Rotated', rotated_rotated)


#resizing
resized=cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow('resize_img',resized)

#flipping
filp_img=cv2.flip(img,-1)
cv2.imshow('flip',filp_img)

#cropped
cropped=img[200:400,300:400]
cv2.imshow('cropp',cropped)







cv2.waitKey(0)
