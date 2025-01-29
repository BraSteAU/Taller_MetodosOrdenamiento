#Ordenación de nombres por longitud: Ordena una lista de nombres según la cantidad de
#caracteres utilizando ordenamiento burbuja.

nombres=input("Ingrese nombres separados por espacios: ").split()
for i in range(len(nombres)):
    nombres[i]=(nombres[i])

n=len(nombres)
for i in range(n-1):
    for j in range(n-1-i):
        if len(nombres[j])>len(nombres[j+1]):
            nombres[j],nombres[j+1]=nombres[j+1],nombres[j]
print(f"Nombres ordenados: {nombres}")