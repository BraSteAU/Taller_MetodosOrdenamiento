#Ordenación de productos por fecha de caducidad: Dado un conjunto de productos con fechas de
# caducidad, ordénalos utilizando el método de heapsort

productos=[
    {"nombre":"arroz","fecha_caducidad":"10-02-2025"},
    {"nombre": "leche", "fecha_caducidad": "2025-01-03"},
    {"nombre": "galletas", "fecha_caducidad": "2025-05-20"},
    {"nombre": "arepas", "fecha_caducidad": "2025-08-15"},
    {"nombre": "huevos", "fecha_caducidad": "2025-06-10"}
]


for producto in productos:
    producto["fecha_numerica"]=int(producto["fecha_caducidad"].replace("-",""))

n=len(productos)
for i in range(n//2-1,-1,-1):
    raiz=i
    while True:
        hijo_izq=2*raiz+1
        hijo_der=2*raiz+2
        mayor=raiz
        if hijo_izq<n and productos[hijo_izq]["fecha_numerica"]>productos[mayor]["fecha_numerica"]:
            mayor=hijo_izq
        if hijo_der < n and productos[hijo_der]["fecha_numerica"] > productos[mayor]["fecha_numerica"]:
            mayor = hijo_der
        if mayor != raiz:
            productos[raiz], productos[mayor] = productos[mayor], productos[raiz]
            raiz = mayor
        else:
            break
for i in range(n - 1, 0, -1):
    productos[0], productos[i] = productos[i], productos[0]
    raiz = 0
    while True:
        hijo_izq = 2 * raiz + 1
        hijo_der = 2 * raiz + 2
        mayor = raiz

        if hijo_izq < i and productos[hijo_izq]["fecha_numerica"] > productos[mayor]["fecha_numerica"]:
            mayor = hijo_izq
        if hijo_der < i and productos[hijo_der]["fecha_numerica"] > productos[mayor]["fecha_numerica"]:
            mayor = hijo_der

        if mayor != raiz:
            productos[raiz], productos[mayor] = productos[mayor], productos[raiz]
            raiz = mayor
        else:
            break

for producto in productos:
    print(f"{producto['nombre']} - Fecha de caducidad: {producto['fecha_caducidad']}")


