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

