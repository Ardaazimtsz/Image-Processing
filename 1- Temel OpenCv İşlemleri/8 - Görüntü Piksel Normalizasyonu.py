import cv2 as cv
import numpy as np

path = "Osayi.jpg"
src = cv.imread(path)

print(src.shape)

gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
cv.waitKey(0)
print(gray.shape)
print(gray)

gray = np.float32(gray)
print(gray)

# NORM MİNMAX

print(gray)

means,stddev = cv.meanStdDev(src)
print(means,stddev)

dst = np.zeros(gray.shape,dtype = np.float32)

cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
print(dst)

print(np.uint8(dst*255))

