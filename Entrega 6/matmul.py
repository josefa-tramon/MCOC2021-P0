from numpy import float32
import matplotlib.pylab as plt
import matplotlib.pyplot as plt 
import matplotlib as mpl
from matplotlib import pyplot
import string


caso = ["Completa","Dispersa"]

c_type = ["INV","SPSOLVE"]


for j in caso:

	for C in c_type:

		Ns0 = []

		dts_ens0 = []

		dts_sol0 = []


		fid = open(f"Complejidad Comp. Matriz {j} - {C}.txt" , "r")

		Ns = []

		dts_ens = []

		dts_sol = []

		for line in fid:
			
			sl = line.split()

			N = int(sl[0])
			dt_ens = float32(sl[1])
			dt_sol = float32(sl[2])

			Ns.append(N)
			dts_ens.append(dt_ens)
			dts_sol.append(dt_sol)

		fid.close()

		Ns0.append(Ns)
		dts_ens0.append(dts_ens)
		dts_sol0.append(dts_sol)


		eje_dt_ens0=[1*10**-4, 1*10**-3, 10**-2, 10**-1, 1, 10, 60, 600]
		eje_dt_ens=["0.1ms", "1ms", "10ms","0.1s", "1s", "10s", "1min", "10min"]

		eje_dt_sol0=[1*10**-4, 1*10**-3, 10**-2, 10**-1, 1, 10, 60, 600]
		eje_dt_sol=["0.1ms", "1ms", "10ms","0.1s", "1s", "10s", "1min", "10min"]

		eje_N0=[10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
		eje_N=["10", "20", "50", "100", "200", "500", "1000", "2000", "5000"]


		plt.figure()
		
		plt.subplot(2,1,1)
		plt.ylabel("Tiempo de Ensamblado (s)")
		plt.title(f"Complejidad Computacional - Inverza de Matriz {j} con {C}")

		for i in range(len(Ns0)):
			plt.loglog(Ns0[i], dts_ens0[i],"o-", color = "black", alpha = 0.3)

		pop_ens = []
		for i in range(len(Ns0[0])):
			a = dts_ens0[-1][-1]
			pop_ens.append(a)

		plt.loglog(Ns0[0],pop_ens,"--")															#Recta 1

		print(dts_ens0)

		

		y0 = 0
		y1 = 0
		d = 0
		y10 = 0
		y20 = 0
		y30 = 0
		x0 = 0
		x1 = 0
		m1 = 0
		m2 = 0
		m3 = 0


		y0 = dts_ens0[0][0]
		y1 = dts_ens0[-1][-1]

		d = abs(y1 - y0)

		y10 = y0 - d
		y20 = y10 - d
		y30 = y20 - d

		x0 = Ns0[0][0]
		x1 = Ns0[-1][-1]


		m1 = (y1 - y10)/(x1 - x0)
		m2 = (y1 - y20)/(x1 - x0)
		m3 = (y1 - y30)/(x1 - x0)

		if m1 == 0:
			m1 = 0.00001
		if m2 == 0:
			m2 = 0.00001
		if m1 == 0:
			m3 = 0.00001


		x10 = (-y1/m1) + x1
		x20 = (-y1/m2) + x1
		x30 = (-y1/m3) + x1

		plt.loglog([x0,x1],[y0,y1],"--")
		plt.loglog([x10,x1],[0.00001,y1],"--")
		plt.loglog([x20,x1],[0.00001,y1],"--")
		plt.loglog([x30,x1],[0.00001,y1],"--")


		plt.yticks(eje_dt_ens0,eje_dt_ens)
		plt.xticks(eje_N0)

		plt.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=False)

		plt.subplot(2,1,2)
		plt.xlabel("Tamaño matriz N")
		plt.ylabel("Tiempo de Solución (s)")

		for i in range(len(Ns0)):
			plt.loglog(Ns0[i], dts_sol0[i],"o-", color = "black", alpha = 0.3)
			plt.legend([""])

		pop_sol = []
		for i in range(len(Ns0[0])):
			a = dts_sol0[-1][-1]
			pop_sol.append(a)

		plt.loglog(Ns0[0],pop_sol,"--")															#Recta 1


		y0 = 0
		y1 = 0
		d = 0
		y10 = 0
		y20 = 0
		y30 = 0
		x0 = 0
		x1 = 0
		m1 = 0
		m2 = 0
		m3 = 0


		y0 = dts_sol0[0][0]
		y1 = dts_sol0[-1][-1]

		d = abs(y1 - y0)

		y10 = y0 - d
		y20 = y10 - d
		y30 = y20 - d

		x0 = Ns0[0][0]
		x1 = Ns0[-1][-1]


		m1 = (y1 - y10)/(x1 - x0)
		m2 = (y1 - y20)/(x1 - x0)
		m3 = (y1 - y30)/(x1 - x0)

		if m1 == 0:
			m1 = 0.00001
		if m2 == 0:
			m2 = 0.00001
		if m1 == 0:
			m3 = 0.00001


		x10 = (-y1/m1) + x1
		x20 = (-y1/m2) + x1
		x30 = (-y1/m3) + x1

		plt.loglog([x0,x1],[y0,y1],"--")
		plt.loglog([x10,x1],[0.00001,y1],"--")
		plt.loglog([x20,x1],[0.00001,y1],"--")
		plt.loglog([x30,x1],[0.00001,y1],"--")

		plt.yticks(eje_dt_sol0,eje_dt_sol)
		plt.xticks(eje_N0,eje_N)

		plt.legend(["Constante","O(N)","O({}²)".format("N"),"O({}³)".format("N"),"O({}⁴)".format("N")], loc="lower left")

		plt.show()
