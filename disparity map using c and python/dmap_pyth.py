import numpy as np
import cv2
import math as m
import matplotlib.pyplot as plt
import dispmap_cy
import time

imgL = cv2.imread('pair1-L.png',cv2.IMREAD_GRAYSCALE)
imgR = cv2.imread('pair1-R.png',cv2.IMREAD_GRAYSCALE)
imgL=cv2.resize(imgL,(240,200))
imgR=cv2.resize(imgR,(240,200))
imgL=np.array(imgL,dtype=np.int)
imgR=np.array(imgR,dtype=np.int)
print(imgL.dtype)
sz_win = tuple(map(int, input("Enter space separated values for height and width of the window: ").split()))
step = int(input("Enter the pixel steps: "))
numDisp=int(input("Enter the neighbourhood size of a pixel"))

t1 = time.time()

disp_mapL = dispmap_cy.dispmap(imgL, imgR, sz_win[0], sz_win[1], numDisp, step)

t2 = time.time()
t = t2 - t1
print("%.20f" % t)

plt.imshow(disp_mapL,'gray')
plt.show()