import numpy
cimport numpy
from libc.math cimport pow

DTYPE=numpy.int
ctypedef numpy.int_t DTYPE_t

cimport cython
@cython.boundscheck(False) 
@cython.wraparound(False)
cpdef numpy.ndarray[DTYPE_t, ndim=2] dispmap(numpy.ndarray[DTYPE_t, ndim=2] imgL,numpy.ndarray[DTYPE_t, ndim=2] imgR, int r_w, int c_w, int nbh, int step):
	cdef int r_L=imgL.shape[0]
	cdef int c_L=imgL.shape[1]
	cdef int r_R=imgR.shape[0]
	cdef int c_R=imgR.shape[1]

	cdef numpy.ndarray[DTYPE_t,ndim=2] dmap = numpy.zeros([r_L,c_L], dtype=DTYPE)

	cdef int i,j,k,a,b,pos,max_el=0
	cdef float ssd,sum1

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
			if dmap[i][j]>max_el:
				max_el=dmap[i][j]

	return dmap/max_el

D_TYPE=numpy.float
ctypedef numpy.float_t D_TYPE_t

@cython.boundscheck(False) 
@cython.wraparound(False)
cpdef numpy.ndarray[D_TYPE_t, ndim=2] findispmap(numpy.ndarray[D_TYPE_t, ndim=2] imgL,numpy.ndarray[D_TYPE_t, ndim=2] imgR):
	cdef int r_L=imgL.shape[0]
	cdef int c_L=imgL.shape[1]
	cdef int r_R=imgR.shape[0]
	cdef int c_R=imgR.shape[1]
	cdef float ent

	cdef numpy.ndarray[D_TYPE_t,ndim=2] dmap = numpy.zeros([r_L,c_L], dtype=D_TYPE)

	cdef int i,j
	for i in range(r_L):
		for j in range(c_L):
			ent=(imgL[i,j]+imgR[i,j])/2
			dmap[i,j]=ent

	return dmap
