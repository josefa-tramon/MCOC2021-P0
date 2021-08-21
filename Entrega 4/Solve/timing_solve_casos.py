from scipy import matmul, rand
from time import perf_counter
from scipy.linalg import solve, inv
from numpy import eye, float32, ones, float64

def laplaciana32(N, tipo = float32):
	e = eye(N) - eye(N,N,1)
	return tipo(e + e.T)

def laplaciana64(N, tipo = float64):				#double
	e = eye(N) - eye(N,N,1)
	return tipo(e + e.T)


Ns = [20,30,50,100,110,120,140,160,180,200,500,800,1000,1100,1200,1300,1500]

dts = []

mems = []


def x1(A,b):
	return inv(A)*b

def x2(A, b):
	return solve(A,b)

def x3(A, b):
	return solve(A,b, assume_a= 'pos')

def x4(A, b):
	return solve(A,b, assume_a= 'sym')

def x5(A, b):
	return solve(A,b, overwrite_a = True)

def x6(A, b):
	return solve(A,b, overwrite_b = True)

def x7(A, b):
	return solve(A,b, overwrite_a = True, overwrite_b = True)



d_type = [laplaciana32, laplaciana64]
casos = [x1, x2, x3, x4, x5, x6, x7]


for d in range(len(d_type)):

		for c in range(len(casos)):

			for i in range(10):		


				if d == 0:
					fid = open(f"timing_solve_caso_{c+1}.{i+1}_float.txt" , "w")

				else:
					fid = open(f"timing_solve_caso_{c+1}.{i+1}_double.txt" , "w")

				for N in Ns:

					if d == 0:

						A = laplaciana32(N)

					else: 

						A = laplaciana64(N)


					b = ones(N)

					t1 = perf_counter()
					
					Am1 = casos[c](A, b)

					t2 = perf_counter()


					bytes_total = A.nbytes + Am1.nbytes

					dt = t2 - t1

					fid.write(f"{N} {dt} {bytes_total}\n")

				fid.close()


