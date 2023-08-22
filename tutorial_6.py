import cv2
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv2.imshow('bank_img',blank)
#paint img certain colors
blank[0:200,200:400]=(0,0,255)
cv2.imshow('green',blank)
#draw reactangle
cv2.rectangle(blank,(0,0),(255,255),(0,255,0,),thickness=-1)
cv2.imshow('reactangle',blank)
#draew circle
cv2.circle(blank,(255,255),40,(0,0,255),thickness=-1)
cv2.imshow('circle',blank)

#draw line
cv2.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
cv2.imshow('line',blank)
#put text
cv2.putText(blank,'hello im tejas',(0,255),cv2.FONT_HERSHEY_COMPLEX,1.0,(0,0,255),2)
cv2.imshow('text',blank)

#
cv2.waitKey(0)