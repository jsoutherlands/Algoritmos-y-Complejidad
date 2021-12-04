import numpy as np
import time

case = str(input('Caso: '))
archivo = open('caso'+case+'.txt', 'r')
lineas = archivo.readlines()
for x in range(len(lineas)):
    lineas[x] = lineas[x].strip().split()
    for y in range(len(lineas[x])):
        lineas[x][y] = int(lineas[x][y])
n = lineas[0][0]
A = lineas[1:n+1]
B = lineas[n+1:n*2+1]
C = [[0 for x in range(n)] for y in range(n)] 
start = time.time()
for i in range(n):
    for j in range(n):
        C[i][j] = 0
        for k in range(n):
            C[i][j] += A[i][k]*B[k][j]
end = time.time()

len_C = len(C)
print("Dimensión matriz resultante: " + str(len_C))
for i in C:
    print(i)
print("Tiempo de ejecución: " + str(end-start))
archivo.close()