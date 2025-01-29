#Ordenación de precios de productos: Un sistema de inventario tiene precios desordenados.
#Ordénalos ascendentemente con burbuja.

precios=input("Ingresa los precios de los productos: ").split()
for i in range(len(precios)):
    precios[i]=float(precios[i])

n=len(precios)
for i in range(n):
    for j in range(n-1):
        if precios[j]>precios[j+1]:
            precios[j],precios[j+1]=precios[j+1],precios[j]
print(f"Precios de los productos en orden ascendente: {precios}")
