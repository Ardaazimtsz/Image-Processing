import cv2 as cv
import numpy as np

path = "Osayi.jpg"
src = cv.imread(path,cv.IMREAD_GRAYSCALE)

# MinMaxLoc

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(src)
print(min_value, max_value, min_loc, max_loc)

#meanStdDev

means,stddev = cv.meanStdDev(src)
print(means,stddev)

src[np.where(src<means)] = 0
src[np.where(src>means)] = 255

cv.imshow("Gray",src)
cv.waitKey(0)
cv.destroyAllWindows()