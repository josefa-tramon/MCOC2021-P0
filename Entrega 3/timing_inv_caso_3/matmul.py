import matplotlib.pylab as plt
from numpy import float32

c_type = [ "caso_3_half", "caso_3_single" , "caso_3_double" , "caso_3_longdouble" ]

for C in c_type:

	Ns0 = []

	dts0 = []

	mems0 = []


	for i in range(10):

		fid = open(f"timing_inv_{C}_{i}.txt" , "r")

		Ns = []

		dts = []

		mems = []

		for line in fid:
			
			sl = line.split()

			print(sl)

			N = int(sl[0])
			dt = float32(sl[1])
			mem = int(sl[2])

			Ns.append(N)
			dts.append(dt)
			mems.append(mem)


		fid.close()

		Ns0.append(Ns)
		dts0.append(dts)
		mems0.append(mems)


	eje_dt0=[1*10**-4, 1*10**-3, 10**-2, 10**-1, 1, 10, 60, 600]
	eje_dt=["0.1ms", "1ms", "10ms","0.1s", "1s", "10s", "1min", "10min"]

	eje_mem0=[10**3,10**4,10**5,10**6, 10**7,10**8, 10**9, 10**10, 10**11, 10**12, 10**13]
	eje_mem=["1KB", "10KB", "100KB", "1MB", "10MB", "100MB", "8GB", "10GB", "11GB","12GB", "13GB"]

	eje_N0=[10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
	eje_N=["10", "20", "50", "100", "200", "500", "1000", "2000", "5000", "10000",]


	plt.figure("Uso memoria")

	plt.subplot(2,1,1)

	plt.title(f"Rendimiento INV numpy {C}")

	plt.ylabel("Tiempo transcurrido (s)")


	for i in range(len(Ns0)):
		plt.loglog(Ns0[i], dts0[i],"o-")



	plt.yticks(eje_dt0,eje_dt)
	plt.xticks(eje_N0)

	plt.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=False)
	plt.grid(True)


	plt.subplot(2,1,2)


	plt.xlabel("Tamaño matriz N")
	plt.ylabel("Uso memoria (s)")

	plt.loglog(Ns0[0], mems0[0],"o-") #Solo se usa los primeros datos ya que siempre será constante el uso de espacio en la memoria por parte de las matrices

	plt.axhline(y=1*10**12,color="k",linestyle="--")

	plt.grid(True)

	plt.yticks(eje_mem0,eje_mem)
	plt.xticks(eje_N0,eje_N)


	plt.show()	


