# Resim Yükleme #
from imageio.plugins import opencv

import cv2 as cv
import numpy as np

path = "Osayi.jpg"

img = cv.imread(path)

type(img)

# NamedWindow

cv.namedWindow("opencv_test, cv.WINDOW_AUTOSIZE")

#imgshow

cv.imshow("opencv_test", img)
cv.waitKey(1000)

cv.destroyWindow()


