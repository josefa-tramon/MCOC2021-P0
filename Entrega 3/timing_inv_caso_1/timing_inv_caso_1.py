#timing_inv_caso_1.py

from time import perf_counter
from numpy import zeros, dtype
from numpy import half, single, double, longdouble, float16, float32, float64
from numpy.linalg import inv 

from laplaciana import laplaciana


Ns = [20,30,50,100,110,120,140,160,180,200,500,800,1000,1100,1200,1300,1500]

dts = []

mems = []

c_type = [float8, float16, float32, float64]

for c in c_type:

	for i in range(10):

		type_str = str(c)[1:-2].split('.')[1]

		print(type_str)

		if type_str == "float64":
			fid = open(f"timing_inv_caso_1_longdouble_{i}.txt" , "w")

		elif type_str == "float32":
			fid = open(f"timing_inv_caso_1_double_{i}.txt" , "w")

		elif type_str == "float16":
			fid = open(f"timing_inv_caso_1_single_{i}.txt" , "w")

		else:
			fid = open(f"timing_inv_caso_1_half_{i}.txt" , "w")

		for N in Ns:

			A = laplaciana(N, dtype = c)

			t1 = perf_counter()
			
			Am1 = inv(A)

			t2 = perf_counter()


			bytes_total = A.nbytes + Am1.nbytes

			mems.append(bytes_total)

			dt = t2 - t1

			dts.append(dt)

			fid.write(f"{N} {dt} {bytes_total}\n")

		fid.close()
