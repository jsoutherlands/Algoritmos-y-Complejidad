def busquedabinaria_dosramas(N, M, lista):
    i = 0
    j = N-1
    total = lista[i] + lista[j]
    if total > M:
        return busquedabinaria_dosramas(j,lista[0:len(lista)-1],M)
    elif total < M:
        return busquedabinaria_dosramas(j,lista[1:j],M)
    elif total == M:
        return i+1 , j+1

N =  int(input())
if N < 1 or N > 10000000:
    print("Error: valor de N no cumple restricción.")
    exit()
else:
    lista = input()
    lista = lista.strip().split(" ")
    lista = [int(x) for x in lista]
    M = int(input())
    while(lista[N-1] >= M):
        lista.pop()
        N -= 1
    if N < 1 or N > 10000000:
        print("Error: valor de N no cumple restricción.")
        exit()
    i,j = busquedabinaria_dosramas(N, M, lista)
    if i < j:
        print(i,j)
    else:
        print("Error: 'j' es menor a 'i'.")
        exit()