import cv2
import numpy as np
import matplotlib.pyplot as plt
import os.path

from matplotlib.animation import FuncAnimation
import random


def main():

    roi_file_name = "roi_frame_size.txt"
    cap = cv2.VideoCapture(1)

    roi_selected = False
    if_axis_set = False

    x_tab = []

    if os.path.isfile(roi_file_name):
        roi_selected = True
        
        with open(roi_file_name, 'r') as f:
            r = f.read().split()

    while (True):
        ret, frame = cap.read()

        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        k = cv2.waitKey(20)

        if k & 0xFF == ord('s') and roi_selected == True:
        # if roi_selected:
            shape = cropped.shape
            r_dist = []
            b_dist = []
            g_dist = []
            i_dist = []
            for i in range(shape[1]):
                r_val = np.mean(cropped[:, i][:, 0])
                b_val = np.mean(cropped[:, i][:, 1])
                g_val = np.mean(cropped[:, i][:, 2])
                i_val = (r_val + b_val + g_val) / 3

                r_dist.append(r_val)
                g_dist.append(g_val)
                b_dist.append(b_val)
                i_dist.append(i_val)

            r_d = (np.array(r_dist) / 255) * 100
            g_d = (np.array(g_dist) / 255) * 100
            b_d = (np.array(b_dist) / 255) * 100
            i_d = (np.array(i_dist) / 255) * 100

            min_length = 380
            max_length = 750

            red = 625
            # green = 525
            blue = 460

            if not if_axis_set:        

                red_i_max = max(enumerate(r_d),key=lambda x: x[1])[0]
                blue_i_max = max(enumerate(g_d), key=lambda x: x[1])[0]

                for x in range(len(r_d)):
                    a = (red - blue)/(red_i_max-blue_i_max)
                    x_tab.append(x * a + blue-a*blue_i_max)

                if_axis_set = True

            plt.subplot(2, 1, 1)

            # plt.imshow( frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2]) ] [: , : , ::-1])
            plt.imshow( frame[int(r[0]):int(r[1]), int(r[2]):int(r[3])])

            plt.subplot(2, 1, 2)
            plt.plot(x_tab, r_d, color='r', label='red')
            plt.plot(x_tab, g_d, color='b', label='blue')
            plt.plot(x_tab, b_d, color='g', label='green')
            plt.plot(x_tab, i_d, color='k', label='mean')
            plt.legend(loc="upper left")
            plt.show()


        elif k & 0xFF == ord('r'):
            r = cv2.selectROI(frame)
            roi_selected = True
            if_axis_set = False

            with open(roi_file_name, "w") as f:
                # f.write(f"{int(r[0])} {int(r[1])} {int(r[2])} {int(r[3])}")
                f.write(f"{int(r[1])} {int(r[1] + r[3])} {int(r[0])} {int(r[0] + r[2])}")
            
            with open(roi_file_name, 'r') as f:
                r = f.read().split()


        elif k & 0xFF == ord('q'):
            break

        else:
            if roi_selected:
                # cropped = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
                cropped = frame[int(r[0]):int(r[1]), int(r[2]):int(r[3])]
                cv2.imshow('roi', cropped)
            else:
                cv2.imshow('frame', frame)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()