import numpy as np

def join_alg(N, M ,aM, aN,list1,list2, flag):
    
    ambas = []
 
    #Nested-Loops
    for x in list1:
        for j in list2:
            if x[-1] == j[0]:
                
                for i in range(len(x)):
                    
                    ambas.append(x[i])
                for k in range(len(j)):
                    if k != 0:
                        ambas.append(j[k])
    elem = N + M - 1
    separacion = np.array_split(ambas, len(ambas)/elem)   

    if(flag == 1):
        print(elem)
        for lectura1 in aN:
            print(lectura1, end=" ")
        for lectura2 in aM:
            if lectura2 != aM[0]:
                print(lectura2, end=" ")
        print()
        print(len(separacion))
        for array in separacion:
            for i in array:
                print(str(i), end=" ")
            print()
    return separacion