import numpy as np
from time import perf_counter

def laplaciana_completa(N, t = np. float32):
	e = np.eye(N) - np.eye(N,N,1)
	return t(e+e.T)


Ns = [20,30,50,100,110,120,140,160,180,200,500,800,1000,1100,1200,1300,1500,3000]

dts = []

mems = []



for i in range(10):

	fid = open(f"Complejidad Comp.- Matriz COMPLETA-{i}.txt" , "w")

	for N in Ns:

		t1 = perf_counter()

		A = laplaciana_completa(N)

		B = laplaciana_completa(N)

		t2 = perf_counter()

		C = A@B	

		t3 = perf_counter()


		dt_ens = t2 - t1

		dt_sol = t3 - t2


		print(f"N = {N} dt_ensamblado = {dt_ens} s dt_solucion = {dt_sol}")

		fid.write(f"{N} {dt_ens} {dt_sol}\n")

	fid.close()






