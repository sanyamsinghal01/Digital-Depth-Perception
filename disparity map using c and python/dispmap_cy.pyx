import numpy
cimport numpy
from libc.math cimport pow

DTYPE=numpy.int
ctypedef numpy.int_t DTYPE_t

cimport cython
@cython.boundscheck(False) 
@cython.wraparound(False)
def dispmap(numpy.ndarray[DTYPE_t, ndim=2] imgL,numpy.ndarray[DTYPE_t, ndim=2] imgR, int r_w, int c_w, int nbh, int step):
	cdef int r_L=imgL.shape[0]
	cdef int c_L=imgL.shape[1]
	cdef int r_R=imgR.shape[0]
	cdef int c_R=imgR.shape[1]

	cdef numpy.ndarray[DTYPE_t,ndim=2] dmap=numpy.zeros([r_L,c_L],dtype=DTYPE)

	cdef int i
	cdef int j
	cdef int k
	cdef int pos
	cdef float ssd 
	
	cdef numpy.ndarray[DTYPE_t,ndim=2] sum1=numpy.zeros([1,1],dtype=DTYPE)
	cdef numpy.ndarray[DTYPE_t,ndim=2] winL,winR

	for i in range(r_L):
		for j in range(0,c_L-c_w):
			ssd= pow(2,30)
			pos=0
			for k in range(max(0,j-nbh),min(c_L-c_w,j+nbh),step):
				winL=imgL[i:min(i+r_w+1,r_L),j:j+c_w+1]
				winR=imgR[i:min(i+r_w+1,r_L),k:k+c_w+1]
				sum1[0,0]=numpy.sum(numpy.square(winL-winR))
				if sum1[0,0]<ssd:
					ssd=sum1[0,0]
					pos=abs(k-j)

			dmap[i][j]=pos

	return dmap