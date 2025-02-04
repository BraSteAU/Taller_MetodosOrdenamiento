#Ordenación de distancia entre ciudades: Dado un arreglo con distancias entre ciudades,
#ordénalas de menor a mayor usando inserción.

distancia = input("Ingrese las distancia entre ciudades separadas por espacios: ").split()
for i in range(len(distancia)):
    distancia[i]=float(distancia[i])

for i in range(1,len(distancia)):
    clave=distancia[i]
    j=i-1
    while j>=0 and clave<distancia[j]:
        distancia[j+1]=distancia[j]
        j-=1
    distancia[j+1]=clave
print(f"distancia entre ciudades ordenadas: {distancia}")
