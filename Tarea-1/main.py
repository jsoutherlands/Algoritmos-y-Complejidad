from join import join_alg

#--------------------- JOIN ---------------------------


list1 = []
list2 = []
print("Ingrese la cantidad de atributos de la relacion R")
N = int(input())

while N > 100 or N < 1: #cantidad de atributos
    print("Reingresa N. Debe ser entre 1 y 100")
    N = int(input())

#lista de tuplas de las relaciones R y S

print("Ingrese los atributos atributos de forma creciente")
aN = input().replace(" ", "")#lista de inputs aN
aN = list(aN) #atributos de N

print("Ingrese la cantidad de tuplas de la relacion R")
NR = int(input()) #número total de tuplas
for r in range(NR):
    x = input().replace(" ", ",")
    list1.append(eval(x))

print("Ingrese la cantidad de atributos de la relacion S")
M = int(input())

print("Ingrese los atributos atributos de forma creciente")
aM = input().replace(" ", "")
aM = list(aM)

print("Ingrese la cantidad de tuplas de la relacion S")
NS = int(input())
for r in range(NS):
    j = input().replace(" ", ",")
    list2.append(eval(j))

join_alg(N,M,aM,aN,list1,list2, 1)

#--------------------- TRIANGULOS ---------------------------

