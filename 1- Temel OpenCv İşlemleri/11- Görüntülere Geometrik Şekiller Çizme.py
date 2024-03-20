import cv2 as cv
import numpy as np

img = np.zeros((512,512,3), np.uint8)

cv.rectangle(img,(100,100),(300,300),(255,0,0),cv.LINE_8,0)
cv.circle(img,(256,256),50,(0,0,255),2,cv.LINE_8,0)
cv.ellipse(img,(256,256),(150,150),360,0,360,(0,255,0),cv.LINE_8,0)
cv.imshow('img',img)
cv.waitKey(0)