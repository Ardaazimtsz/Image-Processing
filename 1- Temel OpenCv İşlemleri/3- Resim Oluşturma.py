# Resim Oluşturma

import cv2 as cv
import numpy as np

path = "Osayi.jpg"
img = cv.imread(path)
cv.namedWindow("colored",cv.WINDOW_AUTOSIZE)
cv.imshow("colored", img)
cv.waitKey(1)

m1  = np.copy(img)

m2 = img

print(type(img))
img[100:200,200:300,:]= 255
cv.imshow("m2",m2)
cv.waitKey(1)

m3 = np.zeros(img.shape, img.dtype)
cv.imshow("m3",m3)
cv.waitKey(1)

m4 = np.zeros([512,512], np.uint8)
cv.imshow("m4",m4)
cv.waitKey(1)

m5 = np.zeros([512,512],np.uint8)
m5[:,:] = 127
cv.imshow("m5",m5)
cv.waitKey()

img = np.ones((512,512,3), np.uint8)
blank_img = (0,0,0)
red = (0,0,255)
green = (0,255,0)

