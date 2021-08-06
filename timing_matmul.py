from numpy import zeros, float32, random
from time import perf_counter
import matplotlib.pylab as plt

#Tamaño
N = 1000


Ns = [20,30,50,100,110,120,140,160,180,200,500,800,1000,1100,1200,1300,1500,2000,3000,5000,6000]

dts = []

mems = []


for i in range(10):

	fid = open(f"rendimiento{i}.txt" , "w")

	for N in Ns:

		A = zeros((N, N), dtype = float32) + 1 

		B = zeros((N, N)) + 2


		t1 = perf_counter()
		C = A@B
		t2 = perf_counter()

		uso_memoria_total = A.nbytes + B.nbytes + C.nbytes

		mems.append(uso_memoria_total)

		dt = t2 - t1

		dts.append(dt)

		print(f"N = {N} dt = {dt} s mem = {uso_memoria_total} bytes floops = {N**3/dt} floops")

		fid.write(f"{N} {dt} {uso_memoria_total}\n")

	fid.close()

