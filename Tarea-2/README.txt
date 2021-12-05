OBSERVACIONES:

	1. Esta tarea debe ser ejecutada en sistema operativo Linux.
	2. Debe tener la librería 'numpy' instalada en su computador. En caso de no tenerla 
	   ejecutar 'pip3 install numpy' en la terminal.

EJECUCIÓN:
	1. Descomprimir archivo "tarea2-Alvarado-Sierra-Southerland.tar.gz"
	2. Abrir terminal.
	3. Navegar hacia la carpeta descomprimida.
	4. Escribir uno de los siguientes comandos:
	
		make run-strassen
		Si se quiere ejecutar el Algoritmo de Strassen.
		
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

		-> Cuidado: Casos 9 y 10 toman tiempo importante en el Algoritmo Clásico.
	6. La matriz resultante se mostrará por pantalla junto con el tiempo de ejecución.