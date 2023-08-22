#put text over on image??
import cv2
img_path=r''
image=cv2.imread(img_path)
image_resize=cv2.resize(image,(1280,720))
text=''
org=(100,200)
font=cv2.FONT_HERSHEY_COMPLEX
fontscale=6
color=(0,0,255)
thickness=3
linetype=cv2.LINE_AA
img_text=cv2.putText(image_resize,text,org,font,fontscale,thickness,linetype,bottomLeftOrigin=False)
cv2.imshow('text_img',img_text)
cv2.waitKey(0)
cv2.destroyAllWindows()
