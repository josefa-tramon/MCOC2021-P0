import matplotlib.pylab as plt
from numpy import float32

Ns = [20,30,50,100,110,120,140,160,180,200,500,800,1000,1100,1200,1300,1500]
d_type = ["float", "double"]
casos = [1,2,3,4,5,6,7]
casos_nom = ["inv","solve","solve assume_a='pos'","solve assume_a='sym'","solve overwrite_a=True","solve overwrite_b=True", "solve overwrite_a=True y overwrite_b=True" ]

sum_dt = 0
sum_mem = 0


for d in d_type:

	Nx = []
	dx = []
	mex = []


	for c in casos:
		
		dtsx = []
		memsx = []	

		Ns0 = []
		dts0 = []
		mems0 = []	

		for i in range(10):		

			
			fid = open(f"timing_solve_caso_{c}.{i+1}_{d}.txt" , "r")

			Ns = []
			dts = []
			mems = []

			for line in fid:
						
				sl = line.split()

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




		for j in range(len(Ns)):


			for i in range(10):
				sum_dt += dts0[i][j]
				sum_mem += mems0[i][j]

			dtsx.append(sum_dt/10)
			memsx.append(sum_mem/10)

			sum_dt = 0
			sum_mem = 0

		if d == "float":

			fid = open(f"timing_solve_caso_{c}_float-PROMEDIOS.txt" , "w")

		elif d == "double":

			fid = open(f"timing_solve_caso_{c}_double-PROMEDIOS.txt" , "w")

		for n in range(len(Ns)):

			N = Ns[n]

			dt = dtsx[n]

			bytes_total = memsx[n]

			fid.write(f"{N} {dt} {bytes_total}\n")

		fid.close()



		eje_dt0=[1*10**-4, 1*10**-3, 10**-2, 10**-1, 1, 10, 60, 600]
		eje_dt=["0.1ms", "1ms", "10ms","0.1s", "1s", "10s", "1min", "10min"]

		eje_mem0=[10**3,10**4,10**5,10**6, 10**7,10**8, 10**9, 10**10, 10**11, 10**12, 10**13]
		eje_mem=["1KB", "10KB", "100KB", "1MB", "10MB", "100MB", "8GB", "10GB", "11GB","12GB", "13GB"]

		eje_N0=[10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
		eje_N=["10", "20", "50", "100", "200", "500", "1000", "2000", "5000", "10000",]


		plt.figure("Uso memoria")

		plt.subplot(2,1,1)

		plt.title(f"Rendimiento solve {c} {d}")

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

	for C in casos:

		if d == "float":
			fid = open(f"timing_solve_caso_{C}_float-PROMEDIOS.txt" , "r")

		else:
			fid = open(f"timing_solve_caso_{C}_float-PROMEDIOS.txt" , "r")

		Ns1 = []
		dts1 = []
		mems1 = []

		for line in fid:
					
			sl = line.split()

			N = int(sl[0])
			dt = float32(sl[1])
			mem = float32(sl[2])

			Ns1.append(N)
			dts1.append(dt)
			mems1.append(mem)

		fid.close()

		Nx.append(Ns1)
		dx.append(dts1)
		mex.append(mems1)


		eje_dt0=[1*10**-4, 1*10**-3, 10**-2, 10**-1, 1, 10, 60, 600]
		eje_dt=["0.1ms", "1ms", "10ms","0.1s", "1s", "10s", "1min", "10min"]

		eje_mem0=[10**3,10**4,10**5,10**6, 10**7,10**8, 10**9, 10**10, 10**11, 10**12, 10**13]
		eje_mem=["1KB", "10KB", "100KB", "1MB", "10MB", "100MB", "8GB", "10GB", "11GB","12GB", "13GB"]

		eje_N0=[10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
		eje_N=["10", "20", "50", "100", "200", "500", "1000", "2000", "5000", "10000",]


		plt.figure("Uso memoria")

		plt.subplot()

		plt.title(f"Rendimientos Solve {d}")

		plt.legend([f"A_invB_{casos_nom[0]}", f"A_invB_{casos_nom[1]}", f"A_invB_{casos_nom[2]}", f"A_invB_{casos_nom[3]}", f"A_invB_{casos_nom[4]}", f"A_invB_{casos_nom[5]}", f"A_invB_{casos_nom[6]}"])

		plt.ylabel("Tiempo transcurrido (s)")
		plt.xlabel("Tamaño matriz N")
		
		for i in range(len(Nx)):
			plt.loglog(Nx[i], dx[i],"o-")
		

		plt.yticks(eje_dt0,eje_dt)
		plt.xticks(eje_N0)
		

		plt.grid(True)


	plt.show()




