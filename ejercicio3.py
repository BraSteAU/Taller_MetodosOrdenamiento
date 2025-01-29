#Temperaturas diarias: Un sensor registra las temperaturas de una semana. Ordena los valores
#de mayor a menor utilizando burbuja.

temperatura=input("Ingrese los 7 registros de temperatura de la semana: ").split()
for i in range(len(temperatura)):
    temperatura[i]=int(temperatura[i])

n=len(temperatura)
for i in range(n):
    for j in range(n-1):
        if temperatura[j]<temperatura[j+1]:
            temperatura[j],temperatura[j+1]=temperatura[j+1],temperatura[j]
print(f"Temperaturas de la semana en orden descendente: {temperatura}")