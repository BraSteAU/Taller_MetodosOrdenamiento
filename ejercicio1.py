#Ordenación de notas de estudiantes: Dado un arreglo de calificaciones, ordénalas de menor a
#mayor usando el método de burbuja.

calificaciones=input("Ingrese 5 calificaciones separadas por espacios: ").split()
for i in range(len(calificaciones)):
    calificaciones[i]=float(calificaciones[i])

n=len(calificaciones)
for i in range(n-1):
    for j in range(n-1-i):
        if calificaciones[j]>calificaciones[j+1]:
            calificaciones[j],calificaciones[j+1]=calificaciones[j+1],calificaciones[j]
print(f"Calificaciones ordenadas: {calificaciones}")