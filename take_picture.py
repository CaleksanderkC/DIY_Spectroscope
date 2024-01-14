import cv2
import numpy as np

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

frame = []
if vc.isOpened():
    rval, frame = vc.read()
    width = vc.get(3)
    height = vc.get(4)
    print(width, height)

else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()

    key = cv2.waitKey(20)
    if key == 27:
        break

min_x = np.inf
max_x = 0
min_y = np.inf
max_y = 0
control_sec = 125

for x, i in enumerate(frame):
    for y, j in enumerate(i):
        if np.sum(frame[x, y]) >= control_sec:
            if(x > max_x):
                max_x = x
            if(y > max_y):
                max_y = y
            if (x < min_x):
                min_x = x
            if (y < min_y):
                min_y = y

frame2 = frame[min_x:max_x, min_y:max_y]

while True:
    cv2.imshow("asd", frame2)
    key = cv2.waitKey(20)

    if key == 27:
        cv2.imwrite('image.png', frame2)
        break

vc.release()
cv2.destroyWindow("preview")
