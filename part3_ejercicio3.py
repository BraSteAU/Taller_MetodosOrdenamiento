#Lista de números aleatorios: Genera una lista de 20 números aleatorios y ordénalos con el
#algoritmo de mergesort

import random
lista = [random.randint(0,100) for i in range(20)]
print(f"Lista desordenada: {lista}")
n=len(lista)
sublista=1

while sublista<n:
    for i in range(0,n,sublista*2):
        izquierda=lista[i:i+sublista]
        derecha=lista[i+sublista:i+sublista*2]
        izq=0
        der=0
        resultado=[]
    
        while izq<len(izquierda) and der<len(derecha):
            if izquierda[izq]<derecha[der]:
                resultado.append(izquierda[izq])
                izq+=1
            else:
                resultado.append(derecha[der])
                der+=1
        resultado+=izquierda[izq:]
        resultado+=derecha[der:]
        lista[i:i+sublista*2]=resultado
    sublista*=2

print(f"Lista ordenada: {lista}")
