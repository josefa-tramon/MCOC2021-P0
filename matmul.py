import matplotlib.pylab as plt

fid = open("rendimiento.txt" , "r")

for line in fid:
	sl = line.split()
	N = int(sl[0])
	dt = int(sl[1])
	mem = int(sl[2])

	Ns.append(N)
	dts.append(dt)
	mems.append(mem)

	print(sl)

fid.close()

plt.figure(1)

plt.subplot(2,1,1)
plt.loglog(Ns, dts)

plt.subplot(2,1,2)
plt.loglog(Ns, mems)

plt.show()


