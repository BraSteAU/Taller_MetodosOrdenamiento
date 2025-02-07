#Ordenación de nombres por orden alfabético inverso: Usa el método de shell sort para ordenar
#una lista de nombres en orden descendente

nombres=input("Ingrese nombres aleatorios ").split()
for i in range(len(nombres)):
    nombres[i]=(nombres[i])

n=len(nombres)
gap=n//2

while gap>0:
    for i in range(gap,n):
        temp=nombres[i]
        j=i
        while j>=gap and nombres[j-gap]>temp:
            nombres[j]=nombres[j-gap]
            j-=gap
        nombres[j]=temp
    gap//=2
print("Lista ordenada ",nombres)
