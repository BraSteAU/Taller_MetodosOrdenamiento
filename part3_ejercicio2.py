#Ordenación de puntajes deportivos: Ordena una lista de puntajes deportivos utilizando el método
#de quicksort

puntajes=input("Ingrese los puntajes ").split()
for i in range(len(puntajes)):
    puntajes[i]=int(puntajes[i])

inicio=0
fin=len(puntajes)-1

anterior=inicio
posterior=fin
pivot=puntajes[inicio]

while anterior<posterior:
    while anterior<posterior and puntajes[posterior]>pivot:
        posterior-=1
    if anterior<posterior:
        puntajes[anterior]=puntajes[posterior]
        anterior+=1
    while anterior<posterior and puntajes[anterior]<=pivot:
        anterior+=1
    if anterior<posterior:
        puntajes[posterior]=puntajes[anterior]
        posterior-=1
    puntajes[anterior]=pivot
    
print(f"Puntajes ordenados: {puntajes}")
     


