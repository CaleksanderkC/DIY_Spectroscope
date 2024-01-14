import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = "frame_screenshot_14.01.2024.png"
image = cv2.imread(file_name)

r = []
rx = []

g = []
gx = []

b = []
bx = []

elcount = 1
for x, i in enumerate(image):

    elcount = x+1
    for y, j in enumerate(i):
        if(x == 0):
            r.append(j[2])
            g.append(j[1])
            b.append(j[0])
            rx.append(y)
        else:
            r[y] = r[y] + int(j[2])
            g[y] = g[y] + int(j[1])
            b[y] = b[y] + int(j[0])

for x in range(len(r)):
    r[x] = r[x]/elcount
    g[x] = g[x] / elcount
    b[x] = b[x] / elcount


plt.plot(rx, r, color="red")
plt.plot(rx, g, color="green")
plt.plot(rx, b, color="blue")

plt.show()
