import numpy as np
from time import perf_counter

def laplaciana_completa(N, t = np. float32):
	e = np.eye(N) - np.eye(N,N,1)
	return t(e+e.T)