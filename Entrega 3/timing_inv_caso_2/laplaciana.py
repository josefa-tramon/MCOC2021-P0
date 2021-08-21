from numpy import zeros
from numpy import dtype

def laplaciana(N, dtype):

	A = zeros((N,N) , dtype = dtype)
	for i in range(N):
		if i>0 and i<(N-1) :
			
			A[i,i] = 2
			A[i+1,i] = -1
			A[i-1,i] = -1

		else:
			A[0,0] = 2
			A[N-1,N-1] = 2 
			A[1,0] = -1
			A[N-2, N-1] = -1
	
	return A