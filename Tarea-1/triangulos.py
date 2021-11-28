from join import join_alg

print("Ingrese arcos (formato A B)")
arco = input().replace(" ",",")
contadorArcos = 1
larcos = []
contador = 0
while arco != "":
    contadorArcos +=1
    larcos.append(eval(arco))
    arco = input().replace(" ",",")

larcos2 = larcos

larcos3 = join_alg(2, 2, [0,1], [1,2], larcos, larcos2, 0)

larcos4 = join_alg(3, 2, [0,1,2], [2,3], larcos3, larcos, 0)

for i in larcos4:
    if i[0] == i[-1]:
        contador +=1

print(int(contador//3))