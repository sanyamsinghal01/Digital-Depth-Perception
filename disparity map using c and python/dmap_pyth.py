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
disp_mapL = np.array(disp_mapL,dtype=np.float)
disp_mapR = dispmap_cy.dispmap(imgR, imgL, sz_win[0], sz_win[1], numDisp, step)
disp_mapR = np.array(disp_mapR,dtype=np.float)
dmapfinal=dispmap_cy.findispmap(disp_mapL,disp_mapR)

t2 = time.time()
plt.imshow(dmapfinal,'gray')
plt.show()

t = t2 - t1
print("Time taken by Cython: {} seconds".format(t))


def dispmappy(imgL, imgR, sz_win, numDisp, step):
  sz_imgL = imgL.shape
  sz_imgR = imgR.shape

  dmap=np.zeros(sz_imgL)
  for i in range(sz_imgL[0]):
    for j in range(0,sz_imgL[1]-sz_win[1]):
      ssd = [m.inf, 0]
      for l in range(max(0, j-numDisp),min(sz_imgL[1]-sz_win[1], j+numDisp), step):
          sum1 = 0
          winL = imgL[i:min(i+sz_win[0]+1, sz_imgL[0]), j:j+sz_win[1]+1]
          winR = imgR[i:min(i+sz_win[0]+1, sz_imgL[0]), l:l+sz_win[1]+1]
          sum1=np.sum(np.square(winL-winR))
          if sum1<ssd[0]:
            ssd = [sum1, abs(l-j)]

      dmap[i][j] = ssd[1]
  return dmap

def ndmap(disp_map):
  maximum = np.amax(disp_map)
  disp_map = (disp_map*255)//maximum
  return disp_map

def dmapfin(dl,dr):
	dmap=np.zeros(dl.shape)
	for i in range(dl.shape[0]):
		for j in range(dl.shape[1]):
			dmap[i,j]=(dl[i,j]+dl[i,j])/2

	return dmap

t3 = time.time()

disp_mapL = ndmap(dispmappy(imgL, imgR, sz_win, numDisp, step))
disp_mapR = ndmap(dispmappy(imgR, imgL, sz_win, numDisp, step))
dmapfinal=dmapfin(disp_mapL,disp_mapR)

t4 = time.time()
plt.imshow(dmapfinal,'gray')
plt.show()
t_py = t4 - t3
print("Time taken by Python: {} seconds".format(t_py))