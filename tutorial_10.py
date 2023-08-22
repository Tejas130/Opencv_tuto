import cv2
import numpy as np

blank=np.zeros((400,400),dtype='uint8')
reactangle=cv2.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv2.circle(blank.copy(),(200,200),200,255,-1)
# cv2.imshow('Rectangle', reactangle)
# cv2.imshow('Circle', circle)

#bitwise and reactangle
bit_and=cv2.bitwise_and(reactangle,circle)
cv2.imshow('bit_and',bit_and)
# bitwise OR --> non-intersecting and intersecting regions
bit_or=cv2.bitwise_or(reactangle,circle)
cv2.imshow('bit_or',bit_or)
#
bit_not=cv2.bitwise_not(circle)
cv2.imshow('bit_not',bit_not)

## bitwise XOR --> non-intersecting regions
bit_xor=cv2.bitwise_xor(reactangle,circle)
cv2.imshow('bit_xor',bit_xor)










cv2.waitKey(0)