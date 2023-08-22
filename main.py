import cv2
#print("version opencv:",cv2.__version__)
#cntrl+/ for multiple comment
#how to show image?????
# path=r'C:\Users\Tejas\Downloads\images (15).jpeg'
# img=cv2.imread(path)
# cv2.imshow('Almond_img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#resize image?????
# path=r'C:\Users\Tejas\Pictures\Saved Pictures\IMG_20220114_200513.JPG'
# img=cv2.imread(path)
# img_size=cv2.resize(img,(600,400))
# cv2.imshow('stat_img',img_size)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#show slide of images?????
import os
import cv2
import numpy as np

# # Specify the directory containing the images
# image_directory = r'C:\Users\Tejas\Pictures\Screenshots'
#
# # Get a list of image file names in the directory
# img_names = os.listdir(image_directory)
#
# # Loop through the image files
# for img_name in img_names:
#     img_path = os.path.join(image_directory, img_name)
#
#     # Check if the file is actually an image (filtering out non-image files)
#     if not os.path.isfile(img_path) or not img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
#         continue
#
#     # Read the image
#     img = cv2.imread(img_path)
#
#     # Check if the image was loaded successfully
#     if img is None:
#         print(f"Error reading image: {img_path}")
#         continue
#
#     # Resize the image
#     img_size = cv2.resize(img, (600, 400))
#
#     # Display the resized image
#     cv2.imshow('Resized Image', img_size)
#
#     # Add a delay to show the image and allow time for user interaction
#     cv2.waitKey(0)  # Use 0 to wait until a key is pressed
#
# # Close all windows after processing
# cv2.destroyAllWindows()

#one img show 4 time in one window?????
# import numpy as np
# img_directory=r'C:\Users\Tejas\Pictures\Screenshots'
# img_names=os.listdir(img_directory)
# for img in img_names:
#     img_path=os.path.join(img_directory,img)
#     img_read=cv2.imread(img_path)
#     img_size=cv2.resize(img_read,(300,300))
#     img_2=np.hstack((img_size,img_size))
#     img_4=np.vstack((img_2,img_2))
#     cv2.imshow('4_image',img_4)
#     cv2.waitKey(0)
# cv2.destroyAllWindows()

