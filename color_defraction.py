import cv2
import numpy as np
from matplotlib import pyplot as plt

file_name = "image.png"

image = cv2.imread(file_name)



r = []
rx = []

g = []
gx = []

b = []
bx = []


for x, i in enumerate(image):
    for y, j in enumerate(i):
        rx.append(y)
        r.append(j[2])


        gx.append(y)
        g.append(j[1])

        bx.append(y)
        b.append(j[0])


plt.scatter(rx, r, color="red")
plt.scatter(gx, g, color="green")
plt.scatter(bx, b, color="blue")

plt.show()

# while True:
#     cv2.imshow("preview", hsvImage)
#
#     key = cv2.waitKey(20)
#     if key == 27:
#         break