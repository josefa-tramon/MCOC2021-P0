from numpy import *
import scipy.sparse as sp
import scipy.sparse.linalg as lin
from scipy.linalg import inv
from laplaciana_sparse import laplaciana
from laplaciana_completa import laplaciana_completa
from time import perf_counter


Ns = [20,30,50,100,110,120,140,160,180,200,500,800,1000,1100,1200,1300,1500,3000]

dts = []

mems = []


caso = ["Completa","Dispersa"]


for j in caso:

	fid = open(f"Complejidad Comp. Matriz {j} - INV.txt" , "w")

	for i in range(10):


		for N in Ns:


			t1 = perf_counter()

			if j == "Dispersa":

				Aa = laplaciana(N, double)

				A = sp.csr_matrix(Aa)

				t2 = perf_counter()

				x = lin.inv(A)

				t3 = perf_counter()


			elif j == "Completa":

				A = laplaciana_completa(N)

				t2 = perf_counter()

				x = inv(A)

				t3 = perf_counter()



			dt_ens = t2 - t1

			dt_sol = t3 - t2


			print(f"N = {N} dt_ensamblado = {dt_ens} s dt_solucion = {dt_sol}")

			fid.write(f"{N} {dt_ens} {dt_sol}\n")


fid.close()






