#Ordenación de ventas diarias: Se registraron ventas diarias de una tienda. Ordénalas en orden
#ascendente con inserción.

ventas=input("Ingrese las ventas diarias separadas por espacios: ").split()
for i in range(len(ventas)):
    ventas[i]=float(ventas[i])

for i in range(1,len(ventas)):
    clave=ventas[i]
    j=i-1
    while j>0 and clave<ventas[j]:
        ventas[j+1]=ventas[j]
        j-=1
    ventas[j+1]=clave
print(f"Ventas de diarias ordenadas: {ventas}")