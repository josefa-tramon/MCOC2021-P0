# MCOC2021-P0

P01:

# Mi computador principal

* Marca/modelo: DESKTOP-RV7HP2N
* Tipo: Notebook
* Año adquisición: 2018
* Procesador:
  * Marca/Modelo: Intel Core i5-7200U
  * Velocidad Base: 2,71 GHz
  * Velocidad Máxima: 2,71 GHz
  * Numero de núcleos: 2 
  * Humero de hilos: 2
  * Arquitectura: AMD64
  * Set de instrucciones: 
* Tamaño de las cachés del procesador
  * L1: 128 KB
  * L2: 512 KB
  * L3: 3,0 Mb
* Memoria 
  * Total: 12 GB
  * Tipo memoria: DDR4
  * Velocidad 1867 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: AMD Radeon (TM) R5 M330
  * Memoria dedicada: 2048 MB
  * Resolución: 1366x768
* Disco 1: 
  * Marca: ST1000LM035
  * Tipo: Duro
  * Tamaño: 1TB
  * Particiones: 4
  * Sistema de archivos: EXT4
* Disco 2: 
  * Marca: KINGSTON
  * Tipo: SSD
  * Tamaño: 223 GB
  * Particiones: 3
  * Sistema de archivos: EXT4

  
* Dirección MAC de la tarjeta wifi: 42-9F-38-C2-0D-** (por privacidad prefiero no dar completa mi dirección, por si las moscas jaja)
* Dirección IP (Interna, del router): 192.168.1.32
* Dirección IP (Externa, del ISP): 190.196.168.111 
* Proveedor internet: GTD Manquehue.



P02:

¿Cómo difiere del gráfico del profesor/ayudante?
Difieren en el tiempo transcurrido al inicio de la ejecución del programa, siendo más lento en mi computador que en el del profesor/ayudante.


¿A qué se pueden deber las diferencias en cada corrida?
Cada corrida es diferente ya que, aunque el equipo es el mismo, esta realizando diferentes tareas de trasfondo, las cuales segun la prioridad que tienen de realización, afectan el rendimiento del programa.


El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
Esto se puede deber a que el espacio que ocupa una matriz es constante, por lo que si crece, crece linealmente su memoria utilizada, en cambio el tiempo de ejecución de la ponderación de las matrices varía de forma exponencial, al crecer las matrices, la dificultad del problema no varía linealmente, ya que no es constante como el crecimiento de las matrices por separado.


¿Qué versión de python está usando?
Python 3.8

¿Qué versión de numpy está usando?
Numpy 1.20.3


Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar. 
Si, se utilizan los 2 núcleos físicos, y 4 hilos, en un 100% cada uno como se puede ver en la fotografía:

![image](https://user-images.githubusercontent.com/62305749/128537962-7070e57d-fbd6-4316-97c2-e5d283ce8274.png)


El desempeño MATMUL en mi computador es el siguiente:

![Desempeño_MATMUL](https://user-images.githubusercontent.com/62305749/128538229-5f28ada9-ff8c-4898-8522-f43bee897632.png)


Se puede apreciar como los procesadores lógicos, que serían los 4 hilos mencionados previamente, estan mayoritariamente trabajando al 100% de su capacidad, cada uno representado en los graficos. La baja en los graficos y luego subida se debe a la variaci{on de matrices que se estan trabajando en el programa, siendo las de menor tamaño primero, y luego las de mayor tamaño, produciendo el uso completo del CPU.


P03:

¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta. 

* El método de numpy utiliza el algoritmo de Gauss - Jordan, en el cual se encuentra la inversa de una matriz a traves ecuaciones, donde el numero de ecuaciones sera el mismo al número de incognitas, las cuales pertenecerán a la matriz inversa de una matriz A conocida. Esto se encuentra al multiplicar la matriz A conocida con la matriz identidad I, y despejando la solución correspondiente. 

* El método de Scipy utiliza el algoritmo de Gauss - Jordan, igual que el método de numpy.

  Para el caso 2: overwrite_a = True , se sobreescribira el resultado obtenido en la misma matriz A, dentro del sistema, lo cual es "más beneficioso" ya que se reutiliza espacio previamente ocupado por la matriz A original. a veces se cumple y otras no, todo dependerá de cuan especifico son los resultados esperados.
  
  Para el caso 3: overwrite_a = False , No se sobreescribira el resultado obtenido, sino que se ocupará nuevo espacio para escribir el resultado (matriz inversa), en la memoria del sistema, por lo que debería ser menos eficiente.



¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 

* Cuando el equipo resuelve varios trabajos simultaneamente, y por lo mismo, genera cierta "jerarquización" sobre las tareas más importantes a las de menor relevancia, para así ejecutar lo que considera mas relevante terminar primero.



RESULTADOS OBTENIDOS:


*CASO 1: Los casos 1 (numpy.inv) para half y single no fueron posibles ya que los resultados son poco exactos, y al utilizar este metodo, el programa primero ejecuta los calculos con d_type float 32, y luego aproxima más estos resultados, no realizandolo con menos decimales ya que no realiza calculos con tan poca especificidad.

![caso_1_longdouble](https://user-images.githubusercontent.com/62305749/130003442-de9bb855-4191-4891-a1f4-d770e9d89d8e.png)
![caso_1_double](https://user-images.githubusercontent.com/62305749/130003444-e051fe81-f1e3-4b66-97c5-d034d9b91de0.png)



CASO 2:

![caso_2_longdouble](https://user-images.githubusercontent.com/62305749/130003433-efde644c-5396-45f5-939c-6dea92861864.png)
![caso_2_double](https://user-images.githubusercontent.com/62305749/130003436-31d31767-5049-4353-a53f-af020a8a18d6.png)
![caso_2_single](https://user-images.githubusercontent.com/62305749/130003437-7a35aa11-01a9-481b-9081-adb17438392b.png)
![caso_2_half](https://user-images.githubusercontent.com/62305749/130003439-79f3d580-fafe-4dc7-a140-d149582c37ad.png)



CASO 3:

![caso_3_longdouble](https://user-images.githubusercontent.com/62305749/130003445-963eb2ab-b316-4f19-ac9d-9324825c4aad.png)
![caso_3_double](https://user-images.githubusercontent.com/62305749/130003448-28f01583-ca60-4711-93e7-53b48f98f3d2.png)
![caso_3_single](https://user-images.githubusercontent.com/62305749/130003449-a2131988-9fba-4b3c-91ec-3e1e477cfba6.png)
![caso_3_half](https://user-images.githubusercontent.com/62305749/130003450-0606043f-72d9-403d-bb4d-4eba8432d3bc.png)



COMPORTAMIENTO EQUIPO DURANTE PROCESOS:


Se puede ver el uso completo de la CPU al procesar los calculos solicitados.
![CPU](https://user-images.githubusercontent.com/62305749/130003582-34ce0d03-da3d-4d8d-86a4-e6c0cf084bf3.jpeg)

El uso de memoria fue de un 50% aproximadamente.
![Memoria](https://user-images.githubusercontent.com/62305749/130003583-e65ac1cc-a0a5-4fa0-9cfd-ba6218be4891.jpeg)



