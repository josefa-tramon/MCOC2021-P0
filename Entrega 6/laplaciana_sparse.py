from numpy import float64, zeros
import scipy.sparse as sparse


def laplaciana (N, t = float64):
	d = sparse.eye(N,N,1,dtype=t)
	
	print(2*sparse.eye(N, dtype=t) - d - d.T)

	return 2*sparse.eye(N, dtype=t) - d - d.T