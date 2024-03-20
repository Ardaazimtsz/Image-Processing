# Gray İmage #

import cv2 as cv

path = "Osayi.jpg"

img = cv.imread(path)
cv.namedWindow("colored",cv.WINDOW_AUTOSIZE)
cv.imshow("colored", img)
cv.waitKey()

# Cvt Color

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.namedWindow("Gray",cv.WINDOW_AUTOSIZE)
cv.imshow("Gray",gray)
cv.waitKey()

#imwrite

cv.imwrite(path+ "gray_osayi" ,gray)
cv.destroyWindow()

img = cv.imread(path + "Osayi.jpg",cv.IMREAD_GRAYSCALE)
cv.namedWindow("Gray",cv.WINDOW_AUTOSIZE)
cv.imshow("Gray",gray)
cv.waitKey(1)