OBSERVACIONES:

	1. Esta tarea debe ser ejecutada en sistema operativo Linux.
	2. La librería "time" se usa solo para medir los tiempos de ejecución
		y no en la resolución del algoritmo. La única excepción es strassenNumpy.py,
		que es la resolución del Algoritmo de Strassen usando numpy.
	3. IMPORTANTE: strassenNumpy.py fue implementado antes de saber que no se podía
					usar la librería numpy. Como grupo decidimos mantenerla pero bajo
					el nombre que tiene ahora, **y solo es usada para tener otro punto
					de vista en el informe**, es decir, NO es la implementación oficial.

EJECUCIÓN:
	1. Descomprimir archivo "tarea2-Alvarado-Sierra-Southerland.tar.gz"
	2. Abrir terminal.
	3. Navegar hacia la carpeta descomprimida.
	4. Escribir uno de los siguientes comandos:
	
		make run-strassen
		Si se quiere ejecutar el Algoritmo de Strassen implementado manualmente. (Implementación oficial)

		make run-strassenNumpy
		Si se quiere ejecutar el Algoritmo de Strassen implementado con numpy.
		
		make run-tradicional
		Si se quiere ejecutar el Algoritmo Clásico de Multiplicación de Matrices.
	5. Escribir el número de caso a probar:
		1: Matriz n = 2
		2: Matriz n = 5
		3: Matriz n = 15
		4: Matriz n = 30
		5: Matriz n = 50
		6: Matriz n = 100
		7: Matriz n = 200
		8: Matriz n = 500
		9: Matriz n = 1000

		-> Cuidado: Casos 8 y 9 toman tiempo importante en el Algoritmo Clásico.
	6. La matriz resultante se mostrará por pantalla junto con el tiempo de ejecución.