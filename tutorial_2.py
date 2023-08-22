import os
import numpy as np
import cv2

height=720
width=1280
channel=3
fps=30 #frame per sec
sec=5

# fourcc = cv2.VideoWriter_fourcc(*'MP42') # you can split also
# video=cv2.VideoWriter('test.mp4',fourcc,float(fps),(width,height))
#
# for i in range(fps*sec):
#     img=np.random.randint(0,255,(height,width,channel),dtype=np.uint8)
#     video.write(img)
# video.release()

#video frim image??

fourcc=cv2.VideoWriter_fourcc(*'MP42')
video=cv2.VideoWriter('test.mp4',fourcc,float(fps),(width,height))
directory= r''
img_name_list=os.listdir(directory)

for i in range(fps*sec):
    img_name=np.random.choice(img_name_list)
    img_path=os.path.join(directory,img_name)
    img_read=cv2.imread(img_path)
    img_resize=cv2.resize(img_read,(width,height))
    video.write(img_resize)
video.release()
