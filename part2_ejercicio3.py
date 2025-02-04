#Ordenación de caracteres en una palabra: Dada una palabra, ordénala alfabéticamente utilizando
#el método de inserción.

palabra=input("Ingrese una palabra: ")
palabra = list(palabra)
for i in range(1,len(palabra)):
    clave=palabra[i]
    j=i-1
    while j>=0 and clave<palabra[j]:
        palabra[j+1]=palabra[j]
        j-=1
    palabra[j+1]=clave
print("Palabra ordenada ",palabra)