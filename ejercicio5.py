#Ordenación de precios de productos: Un sistema de inventario tiene precios desordenados.
#Ordénalos ascendentemente con burbuja.

precios=[10450.4, 10000.45, 5700.99, 24500.57, 14999.99, 2145.36]

n=len(precios)
for i in range(n):
    for j in range(n-1):
        if precios[j]>precios[j+1]:
            precios[j],precios[j+1]=precios[j+1],precios[j]
print(f"Precios de los productos en orden ascendente: {precios}")
