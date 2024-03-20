import cv2 as cv
import numpy as np

path1 = "Osayi orj.jpg"
path2 = "osayi-Logo.png"
img1 = cv.imread(path1)
img2 = cv.imread(path2)

cv.imshow("osayi1",img1)
cv.waitKey()
cv.imshow("osayi2",img2)
cv.waitKey()

horizontal = np.hstack((img1,img2))
cv.imshow("birleştirilmiş",horizontal)
cv.waitKey()
cv.destroyAllWindows()