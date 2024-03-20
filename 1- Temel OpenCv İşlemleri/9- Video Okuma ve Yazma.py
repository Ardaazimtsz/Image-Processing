import cv2 as cv
import numpy as np

capture = cv.VideoCapture("Trafik Kazaları (mayıs 2023) Crash.mp4")
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
count = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
fps = capture.get(cv.CAP_PROP_FPS)
print(height, width, count, fps)

out = cv.VideoWriter('output_video.avi', cv.VideoWriter_fourcc(*'MJPG'), fps, (width, height), True)

while True:
    ret, frame = capture.read()

    if ret:
        cv.imshow("video-input", frame)
        out.write(frame)
        c = cv.waitKey(1)
        if c == 27:
            break
    else:
        break

capture.release()
out.release()
cv.destroyAllWindows()
