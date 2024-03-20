import cv2 as cv

capture = cv.VideoCapture(0)

height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
count = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
fps = capture.get(cv.CAP_PROP_FPS)
print(height, width, count, fps)

def process(image,opt=1):
    dst = None
    if opt == 0:
        dst = cv.bitwise_not(image)
    if opt == 1:
        dst = cv.GaussianBlur(image, (0, 0), 15)
    if opt == 2:
        dst = cv.Canny(image, 100, 200)
    return dst

while True:
    ret, frame = capture.read()

    if ret:
        cv.imshow("video-input", frame)
        out.write(frame)
        c = cv.waitKey(1)
        if c >= 50:
            index = c - 49
        result = process(frame,index)
        cv.imshow("result", result)
        # print(c)
        if c == 27:
            break
    else:
        break

cv.waitKey(1)
