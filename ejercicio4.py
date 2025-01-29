#Orden de llegada de corredores: Dado un listado de tiempos de llegada en una carrera,
#ordénalos de menor a mayor usando burbuja.

tiempos=input("Ingresa los tiempos de los corredores: ").split()
for i in range(len(tiempos)):
    tiempos[i]=float(tiempos[i])

n=len(tiempos)
for i in range(n-1):
    for j in range(n-1-i):
        if tiempos[j]>tiempos[j+1]:
            tiempos[j],tiempos[j+1]=tiempos[j+1],tiempos[j]
print(f"Tiempo de llegada de los corredores: {tiempos}")
