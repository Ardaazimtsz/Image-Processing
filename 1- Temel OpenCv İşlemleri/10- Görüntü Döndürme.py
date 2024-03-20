import cv2 as cv
import numpy as np
path = "Osayi3.jpg"
src = cv.imread(path)

# X Flip
dst1 = cv.flip(src,0)
cv.imshow("dst1",dst1)
cv.waitKey(0)

# Y Flip

dst2 = cv.flip(src,1)
cv.imshow("dst2",dst2)
cv.waitKey(0)

# XY Flip
dst3 = cv.flip(src,-1)
cv.imshow("dst3",dst3)
cv.waitKey(0)