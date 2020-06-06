import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import exmod
import cv2

imgL = cv2.imread('pair1-L.png',cv2.IMREAD_GRAYSCALE)
imgR = cv2.imread('pair1-R.png',cv2.IMREAD_GRAYSCALE)
imgL=cv2.resize(imgL,(240,200))
imgR=cv2.resize(imgR,(240,200))

h_imgL = imgL.shape[0]
w_imgL = imgL.shape[1]
h_imgR = imgR.shape[0]
w_imgR = imgR.shape[1]

sz_win = tuple(map(int, input("Enter space separated values for height and width of the window: ").split()))
step = int(input("Enter the pixel steps: "))
numDisp=int(input("Enter the neighbourhood size of a pixel"))
h_wind=sz_win[0]
w_wind=sz_win[1]

disp_mapL=np.reshape(exmod.dispmap(imgL,imgR,h_imgL,w_imgL,h_imgR,w_imgR,h_wind,w_wind,numDisp,step),imgL.shape)
disp_mapR=np.reshape(exmod.dispmap(imgR,imgL,h_imgR,w_imgR,h_imgL,w_imgL,h_wind,w_wind,numDisp,step),imgR.shape)

sz_imgR = imgR.shape
var_d=0
stop_param=0

for j in range(int(sz_imgR[1]/2),sz_imgR[1]-sz_win[1]):
   var_disp=np.var(disp_map[0:][j:j+int(sz_imgR[1]/slice_size)])
   if var_disp>var_d:
      var_d=var_disp
      stop_param=sz_imgR[1]-sz_win[1]-j

disp_map = np.zeros((200,240-sz_win[1]-stop_param))
for i in range(disp_map.shape[0]):
  for j in range(disp_map.shape[1]):
    disp_map[i][j] = max(disp_mapL[i][j+stop_param],disp_mapR[i][j])
disp_map=cv2.resize(disp_map,(240,200))    
plt.imshow(disp_map,'gray')
plt.show()  
