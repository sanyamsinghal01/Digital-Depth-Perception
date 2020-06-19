import numpy
from math import pow

def dispmap(imgL,imgR,r_w, c_w,nbh,step):
	r_L=imgL.shape[0]
	c_L=imgL.shape[1]
	r_R=imgR.shape[0]
	c_R=imgR.shape[1]

	dmap = numpy.zeros([r_L,c_L])
	for i in range(r_L):
		for j in range(0,c_L-c_w):
			ssd= pow(2,31)-1
			pos=0
			for k in range(max(0,j-nbh),min(c_L-c_w,j+nbh),step):
				sum1=0
				for a in range(i,min(i+r_w+1,r_L)):
					for b in range(k,k+c_w+1):
						sum1+=pow(imgL[a,b]-imgR[a,b+j-k],2)
				if sum1<ssd:
					ssd=sum1
					pos=abs(k-j)

			dmap[i][j]=pos

	return dmap