#Ranking de puntuaciones: Un juego guarda las puntuaciones de jugadores. Ordena las
#puntuaciones en orden descendente usando inserción.

puntuaciones=input("Ingrese las puntuaciones separadas por espacios: ").split()
for i in range(len(puntuaciones)):
    puntuaciones[i]=float(puntuaciones[i])

for i in range(1,len(puntuaciones)):
    clave=puntuaciones[i]
    j=i-1
    while j>=0 and clave>puntuaciones[j]:
        puntuaciones[j+1]=puntuaciones[j]
        j-=1
    puntuaciones[j+1]=clave

print(f"Puntuaciones ordenadas: {puntuaciones}")
