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




P04:

Haga un comentario completo respecto de todo lo que ve en términos de desempeño en cada problema. ¿Como es la variabilidad del tiempo de ejecucion para cada algoritmo? ¿Qué algoritmo gana (en promedio) en cada caso? ¿Depende del tamaño de la matriz? ¿A que se puede deber la superioridad de cada opción? ¿Su computador usa más de un proceso por cada corrida? ¿Que hay del uso de memoria (como crece)? 

*Para Solve:

![Promedios Rendimientos Solve Float](https://user-images.githubusercontent.com/62305749/130311975-b1243992-98dc-468b-9991-4414a5112a64.png)

![Promedios Rendimientos Solve Double](https://user-images.githubusercontent.com/62305749/130311971-28f4ccbd-fa5a-4f6a-a984-f4dec7932dab.png)

Para ambos tipos de d_type utilizados, float y double, se generan los mismos resultados, esto se puede deber, a que los decimales solo generan mayor exactitud de los resultados, y al ser float uno ya bastante exacto, la diferencia con double es mínima.

Si se ven las matrices en crecimiento, el caso que predomina en rendimiento es el 4to, donde Solve tiene a su parametro assume_a = "sym", que trabaja la matríz como si esta fuera simétrica, lo cual se entiende ya que una matríz simétrica tiene ventajas a la hora de generarse su inversa, a diferencia de una que no lo es. Como el programa asume esa condición, le es más facil y rápido trabajar. Las menos eficientes son el caso 7 y 2, lo cual se podría explicar ya que para el primero mencionado, reescribe la matriz a y el vector b, para reutilizar memoria, sin embargo esta acción, mientras mayor es la dimensión de la matríz, más lento el proceso y por tanto, tiene menor rendimiento. Para el primer caso, asume por default, que es una matríz generica, osea no simetrica, y por tanto, su trabajo tambien es poco eficiente. 


*Para Eigh:

![Promedios Rendimientos Eigh Float](https://user-images.githubusercontent.com/62305749/130311973-ece810a2-bb11-4ede-9326-d5e98d4c6507.png)

![Promedios Rendimientos Eigh Double](https://user-images.githubusercontent.com/62305749/130311974-81e0f14f-8b92-4e30-b6c7-c902c01183a5.png)

Al igual que en el calculo de solve, para ambos tipos de d_type utilizados, float y double, se generan los mismos resultados, esto se puede deber, a que los decimales solo generan mayor exactitud de los resultados, y al ser float uno ya bastante exacto, la diferencia con double es mínima.

El caso de mayor eficiencia es en un inicio, con matrices de dimensión menor a 200, es el número 4, donde el parametro driver = "evr", no se sobreescribe la matriz A, pero si el vector b. Posterior a esa dimensión, tiene mayor eficiencia en tiempo el caso 3, donde la unica diferencia con el caso 4 es que el parametro driver = "evd". Esto es porque los driver routines son más o menos eficientes según el procesador, y para este caso, estos funcionan así, siendo el 3 caso, el driver routine que mejor resuelve ecuaciones lineales en el sistema. 

En cuanto al uso de memoria:

![CPU Entrega 4](https://user-images.githubusercontent.com/62305749/130312157-355fd942-c0b5-47ac-a391-c934a07aed71.jpeg)

![Memoria Entrega 4](https://user-images.githubusercontent.com/62305749/130312158-e0c61c80-f84e-4f83-a30c-e300973230f9.jpeg)

Para ambos casos, se utilizan los 4 hilos, y la memoria es utilizada en un 50%. Por ultimo, para las matrices, con el uso de Eigh, su memoria crece linealmente, en cambio en solve, este cálculo ocupa memoria variable, ya que como las dimensiones no crecen linealmente sino que como exponentes, su cambio en el uso de memoria tambien se comporta así.

RESULTADOS CASOS SOLVER:

![Solve 6 Double](https://user-images.githubusercontent.com/62305749/130311853-2ac1b3f1-bf94-4f41-96c7-c0f8f0e2df37.png)
![Solve 5 Float](https://user-images.githubusercontent.com/62305749/130311855-fff3dc39-bb6b-43a9-83e4-18a397f2f743.png)
![Solve 5 Double](https://user-images.githubusercontent.com/62305749/130311856-63798c1c-4cf1-4ce6-b06a-51d5c980546f.png)
![Solve 4 Float](https://user-images.githubusercontent.com/62305749/130311857-0ecb4de9-e203-482b-b277-2b1894bfc451.png)
![Solve 4 Double](https://user-images.githubusercontent.com/62305749/130311859-2ecaa62c-1669-443f-af42-1c08fc248bf9.png)
![Solve 3 Float](https://user-images.githubusercontent.com/62305749/130311860-55f15292-0b97-4475-8c76-d0a80c9a3f51.png)
![Solve 3 Double](https://user-images.githubusercontent.com/62305749/130311861-be26cdf7-05f0-485d-8489-afbc7c1b6eae.png)
![Solve 2 Float](https://user-images.githubusercontent.com/62305749/130311862-097e938a-050e-45d9-9fce-e7a16c46b275.png)
![Solve 2 Double](https://user-images.githubusercontent.com/62305749/130311863-2e94bd36-89aa-47ac-a2bc-053b91817ab7.png)
![Solve 1 Float](https://user-images.githubusercontent.com/62305749/130311864-a807e7e5-49cb-4641-a3ea-2311b39a571f.png)
![Solve 1 Double](https://user-images.githubusercontent.com/62305749/130311866-b5d7bf3f-acb3-4414-91ee-99502f971efb.png)
![Solve 7 Float](https://user-images.githubusercontent.com/62305749/130311868-4a180c40-9998-42d7-8329-68e42e0b7061.png)
![Solve 7 Double](https://user-images.githubusercontent.com/62305749/130311870-dc28ae0a-2632-43d8-a5fe-95ac0f6e2c48.png)
![Solve 6 Float](https://user-images.githubusercontent.com/62305749/130311871-affa0d5d-97d6-4bd3-a009-106021bf09f3.png)




RESULTADOS CASOS EIGH:

![Eigh 4 Float](https://user-images.githubusercontent.com/62305749/130311878-e2762438-90e9-4e62-82ec-f570fe21bf7e.png)
![Eigh 4 Double](https://user-images.githubusercontent.com/62305749/130311880-b6c763d2-98f6-4b67-8535-b3f5e288bae4.png)
![Eigh 3 Float](https://user-images.githubusercontent.com/62305749/130311881-f179d34c-5eec-4be4-8692-e5a1f1ab247c.png)
![Eigh 3 Double](https://user-images.githubusercontent.com/62305749/130311882-fa7c4944-b34c-481b-bdc2-c4b82c780fb9.png)
![Eigh 2 Float](https://user-images.githubusercontent.com/62305749/130311883-bca89524-d548-44c6-8cfd-174c1722887b.png)
![Eigh 2 Double](https://user-images.githubusercontent.com/62305749/130311884-07208e47-161b-442e-b8ce-8c16b2c1ae97.png)
![Eigh 1 Float](https://user-images.githubusercontent.com/62305749/130311885-908142c4-a937-4b39-9b8e-b2fb46af172a.png)
![Eigh 1 Double](https://user-images.githubusercontent.com/62305749/130311886-748e6b3f-9ce8-4cc4-846b-a770c9e8e4ad.png)
![Eigh 5 Float](https://user-images.githubusercontent.com/62305749/130311887-ffd6cae3-8aab-4df8-8062-d278f9b3930a.png)
![Eigh 5 Double](https://user-images.githubusercontent.com/62305749/130311888-ef4eda76-cb24-4f48-a36e-a9b945a4182c.png)





