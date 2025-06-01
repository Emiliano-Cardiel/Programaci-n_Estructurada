'''
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

#Ejemplo 2 Crear una lista de palabras y psoteriormente buscar la coincidencia de una palabra

#Ejemplo 3 Añadir elementos a la lista

#Ejemplo 4 Crear un multidimensional que permita almacenar el nombre y telefono de una agenda
'''
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
import os
os.system("cls")
numeros=[23,34]
print(numeros)

lista="["
for i in numeros:
    lista+=f"{i},"
print(f"{lista}]")

lista="["
for i in range (0,len(numeros)):
    lista+=f"{numeros[i]},"
print(f"{lista}]")

lista="["
i=0
while i<len(numeros):
    lista+=f"{numeros[i]},"
    i+=1
print(f"{lista}]")

#Ejemplo 2 Crear una lista de palabras y psoteriormente buscar la coincidencia de una palabra
os.system("cls")
palabras=["hola","2023","Lebroncito","UTD","True"]
palabras.append("UTD")
print(palabras)
palabra_buscar=input("Dame la palabra a buscar: ")

#1er Forma
if palabra_buscar in palabras:
    print("Si se encontro la palabra en la lista")
else:
    print("No se encontro la palabra en la lista")

#2da Forma Encuentra posicion, cantidad y busca
encontro=False
cuantas=0
posicion=[]
for i in palabras:
    if i==palabra_buscar:
        encontro=True
        cuantas+=1
        posicion.append(palabras.index(i))
if encontro:
    print("Si se encontro la palabra en la lista")
else:
    print("No se encontro la palabra en la lista")

#3da Forma "I" funciona como la posición
encontro=False
posiciones=[]
for i in range (0,len(palabras)):
    if palabras[i]==palabra_buscar:
        encontro=True
        posiciones.append(i)
if encontro:
     print("Si se encontro la palabra en la lista")
else:
     print("No se encontro la palabra en la lista")

#Ejemplo 3 Añadir elementos a la lista
os.system("cls")
numeros=[]

opc="si"
while opc=="si":
    numeros.append(float(input("Dame un numero entero o decimal: ")))
    opc=input("¿Deseas agregar otro número a la lista (si/no)? ").lower()
print(numeros)

#Ejemplo 4 Crear un multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[]