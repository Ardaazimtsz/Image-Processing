import cv2 as cv

path = "Osayi.jpg"

img = cv.imread(path)
cv.namedWindow("colored",cv.WINDOW_AUTOSIZE)
cv.imshow("colored", img)
cv.waitKey(1)

h,w,ch = img.shape
print("h,w,ch",h,w,ch)

for row in range(h):
    for col in range(w):
        b,g,r = img[row,col]
        b = 255- b
        g = 255- g
        r = 255- r
        img[row,col] = (b,g,r)

cv.imshow("output", img)
cv.waitKey(1)