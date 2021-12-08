import time

num_sumres = 0
num_mul = 0
num_assign = 0

def matrix_sumar(matrix_a, matrix_b):
	fila = len(matrix_a)
	columnas = len(matrix_a[0])
	matrix_c = [list() for i in range(fila)]
	for i in range(fila):
		for j in range(columnas):
			matrix_c_temp = matrix_a[i][j] + matrix_b[i][j]
			global num_sumres, num_assign
			num_sumres = num_sumres + 1
			num_assign = num_assign + 1
			matrix_c[i].append(matrix_c_temp)
	return matrix_c

def matrix_restar(matrix_a, matrix_b):
	fila = len(matrix_a)
	columnas = len(matrix_a[0])
	matrix_c = [list() for i in range(fila)]
	for i in range(fila):
		for j in range(columnas):
			matrix_c_temp = matrix_a[i][j] - matrix_b[i][j]
			global num_sumres,num_assign
			num_sumres = num_sumres + 1
			num_assign = num_assign + 1
			matrix_c[i].append(matrix_c_temp)
	return matrix_c

def matrix_dividir(matrix_a, fila, columna):
	largo = len(matrix_a)
	matrix_b = [list() for i in range(largo // 2)]
	k = 0
	for i in range((fila - 1) * largo // 2, fila * largo // 2):
		for j in range((columna - 1) * largo // 2, columna * largo // 2):
			matrix_c_temp = matrix_a[i][j]
			matrix_b[k].append(matrix_c_temp)
		k += 1
	return matrix_b

def matrix_merge(matrix_11, matrix_12, matrix_21, matrix_22):
	largo = len(matrix_11)
	matrix_todos = [list() for i in range(largo * 2)]
	for i in range(largo):
		matrix_todos[i] = matrix_11[i] + matrix_12[i]
	for j in range(largo):
		matrix_todos[largo + j] = matrix_21[j] + matrix_22[j]
	return matrix_todos

def strassen(matrix_a, matrix_b):
	fila = len(matrix_a)
	if fila == 1:
		matrix_todos = [list() for i in range(fila)]
		matrix_todos[0].append(matrix_a[0][0] * matrix_b[0][0])
	elif(fila % 2 ==1):
		matrix_todos = [[0]*fila for y in range(fila)]
		for i in range(fila):
			for j in range(fila):
				matrix_todos[i][j] = 0
				for k in range(fila):
					matrix_todos[i][j] += (matrix_a[i][k]*matrix_b[k][j])
		global num_mul,num_sumres
		num_mul = num_mul + 27
		num_sumres = num_sumres + 18
	else:
		s1 = matrix_restar((matrix_dividir(matrix_b, 1, 2)), (matrix_dividir(matrix_b, 2, 2)))
		s2 = matrix_sumar((matrix_dividir(matrix_a, 1, 1)), (matrix_dividir(matrix_a, 1, 2)))
		s3 = matrix_sumar((matrix_dividir(matrix_a, 2, 1)), (matrix_dividir(matrix_a, 2, 2)))
		s4 = matrix_restar((matrix_dividir(matrix_b, 2, 1)), (matrix_dividir(matrix_b, 1, 1)))
		s5 = matrix_sumar((matrix_dividir(matrix_a, 1, 1)), (matrix_dividir(matrix_a, 2, 2)))
		s6 = matrix_sumar((matrix_dividir(matrix_b, 1, 1)), (matrix_dividir(matrix_b, 2, 2)))
		s7 = matrix_restar((matrix_dividir(matrix_a, 1, 2)), (matrix_dividir(matrix_a, 2, 2)))
		s8 = matrix_sumar((matrix_dividir(matrix_b, 2, 1)), (matrix_dividir(matrix_b, 2, 2)))
		s9 = matrix_restar((matrix_dividir(matrix_a, 1, 1)), (matrix_dividir(matrix_a, 2, 1)))
		s10 = matrix_sumar((matrix_dividir(matrix_b, 1, 1)), (matrix_dividir(matrix_b, 1, 2)))
		p1 = strassen(matrix_dividir(matrix_a, 1, 1), s1)
		p2 = strassen(s2, matrix_dividir(matrix_b, 2, 2))
		p3 = strassen(s3, matrix_dividir(matrix_b, 1, 1))
		p4 = strassen(matrix_dividir(matrix_a, 2, 2), s4)
		p5 = strassen(s5, s6)
		p6 = strassen(s7, s8)
		p7 = strassen(s9, s10)
		c11 = matrix_sumar(matrix_sumar(p5, p4), matrix_restar(p6, p2))
		c12 = matrix_sumar(p1, p2)
		c21 = matrix_sumar(p3, p4)
		c22 = matrix_restar(matrix_sumar(p5, p1), matrix_sumar(p3, p7))
		matrix_todos = matrix_merge(c11, c12, c21, c22)
		global num_assign
		num_assign = num_assign + 22
	return matrix_todos

case = str(input('Caso: '))
archivo = open('Casos/caso'+case+'.txt', 'r')
lineas = archivo.readlines()
for x in range(len(lineas)):
	lineas[x] = lineas[x].strip().split()
	for y in range(len(lineas[x])):
		lineas[x][y] = int(lineas[x][y])
n = lineas[0][0]
A = lineas[1:n+1]
B = lineas[n+1:n*2+1]

start = time.time()
C = strassen(A,B)
end = time.time()

print(str(len(C)))

line = ""
for i in C:
	for j in i:
		line += str(j) + " "
	print(line)
	line = ""

print("Tiempo de ejecución: " + str(end-start))
archivo.close()