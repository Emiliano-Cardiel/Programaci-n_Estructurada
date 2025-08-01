'''
List (Array)
Son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice númerico.

Nota: Sus valores si son modificables.

La lista es una colección ordenada y modificable. Permite miembros duplicados.

'''

import os
os.system("cls")

#Funciones más comunes en las listas
paises=["Mexico","España","Brasil","Canada"]

numeros=[23,45,8,24]

varios=["hola",3.1416,33,True]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)

#Recorrer la lista
#1er forma
for i in paises:
    print(i)

#2do forma
for i in range (0,len(paises)):
    print(paises[i])

lista=""
for i in range (0,len(paises)):
    lista+=f"[{paises[i]}],"
print(lista)

#Ordenar elementos de una lista
paises.sort()
print(paises)
numeros.sort()
print(numeros)
'''
varios.sort() "Manejo de Excepciones"
'''

#Dar la vuelta a una lista
paises.reverse()
print(paises)

varios.reverse()
print(varios)

#Agregar, Insertar, Añadir un elemento a una lista
#1er forma
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Honduras")
print(paises)

paises.sort()
print(paises)

#Eliminar,Borrar,Suprimir un elemento de una lista
#1er forma
paises.pop(4)
print(paises)

#2da forma
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de la lista
print(paises)

print("Brasil" in paises)

#Contar el número de veces que aparece un elemento dentro de una lista

print(numeros)

cuantos=numeros.count(23)
print(cuantos)

numeros.append(23)
cuantos=numeros.count(23)
print(cuantos)

#Cononcer la posición o indice en el que se encuentra un elemento de la lista
paises.reverse()
print(paises)

'''
Si no encuentra un valor salta un manejo de excepciones
'''
posicion=paises.index("Canada")
print(f"El valor de Canada lo encontro en la posición: {posicion}")

#Unir el contenido de una lista dentro de otra lista

print(numeros)
numeros2=[100,200]

print(numeros2)
os.system("cls")
#Crear a partir de las listas de numeros 1 y 2 una resultante y mostrar el contenido ordenado descendetemente

numeros.extend(numeros2)

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)
