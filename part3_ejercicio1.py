#Ordenación de salarios: Dado un conjunto de salarios de empleados, ordénalos utilizando el
#método de selección.

salarios = input("Ingrese los salarios de los empleados: ").split()
for i in range(len(salarios)):
    salarios[i]=int(salarios[i])

n=len(salarios)
for i in range (n):
    for j in range(n-1):
        if salarios[j]>salarios[j+1]:
            salarios[j],salarios[j+1]=salarios[j+1],salarios[j]
print(f"Salarios de empleados: {salarios}")