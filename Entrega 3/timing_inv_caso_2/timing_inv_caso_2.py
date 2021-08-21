#timing_inv_caso_2.py

from time import perf_counter
from numpy import zeros, dtype
from numpy import half, single, double, longdouble, float16, float32, float64
from scipy.linalg import inv 

from laplaciana import laplaciana


Ns = [20,30,50,100,110,120,140,160,180,200,500,800,1000,1100,1200,1300,1500]

dts = []

mems = []

c_type = [half, single, double, longdouble]

for c in c_type:

	for i in range(10):

		type_str = str(c)[1:-2].split('.')[1]

		print(type_str)

		if type_str == "float64":
			fid = open(f"timing_inv_caso_2_longdouble_{i}.txt" , "w")

		elif type_str == "float32":
			fid = open(f"timing_inv_caso_2_double_{i}.txt" , "w")

		elif type_str == "float16":
			fid = open(f"timing_inv_caso_2_single_{i}.txt" , "w")

		else:
			fid = open(f"timing_inv_caso_2_half_{i}.txt" , "w")

		for N in Ns:

			A = laplaciana(N, dtype = c)

			t1 = perf_counter()
			
			Am1 = inv(A, overwrite_a = False)

			t2 = perf_counter()


			bytes_total = A.nbytes + Am1.nbytes

			mems.append(bytes_total)

			dt = t2 - t1

			dts.append(dt)

			fid.write(f"{N} {dt} {bytes_total}\n")

		fid.close()


