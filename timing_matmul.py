from numpy import zeros, float32
from time import perf_counter
import matplotlib.pylab as plt

#Tamaño
N = 1000

Ns = [10,100,1000,10000,20000]

dts = []

mems = []

fid = open("rendimiento.txt" , "w")

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

	print(f"N = {N} , dt = {dt} s , mem = {uso_memoria_total} bytes , floops = {N**3/dt} floops")

	fid.write(f"{N} {dt} {uso_memoria_total}\n ")

fid.close()
