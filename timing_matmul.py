import numpy as np
from numpy import zeros
from time import perf_counter

print("hello world")

a = np.zeros(10)

print(f"a ={a}")  #fstring


#Tamaño
N = 1000
A = zeros((N, N))+1
B = zeros((N, N))+2


t1 = perf_counter()
C = A@B
t2 = perf_counter()


dt = t2 - t1

print(f"dt = {dt} s")