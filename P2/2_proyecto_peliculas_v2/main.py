'''
Crear un proyecto que permita gestionar (administrar) peliculas. 
Colocar un menu de opciones: Agregar, Borrar, Modificar, Mostrar,
Limpiar una lista de peliculas.

Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar diccionarios para almacenar los atributos (nombre, categoria, clasificación, 
genero, idioma) de peliculas
'''

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t .::: GESTION DE PELICULAS :::.\n\n\t 1.-Crear " \
    "\n\t 2.-Borrar \n\t 3.-Mostrar " \
    "\n\t 4.-Agregar Característica \n\t 5.-Modificar Característica " \
    "\n\t 6.-Borrar Característica \n\t 7.-Salir")
    opcion = input("\n\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPelicula()
            peliculas.espereTecla()
        case "2":
            peliculas.borrarPelicula()
            peliculas.espereTecla()
        case "3":
            peliculas.mostrarPelicula()
            peliculas.espereTecla()
        case "4":
            peliculas.agregarCaracteristicaPelicula()
            peliculas.espereTecla()
        case "5":
            peliculas.modificarCaracteristicaPelicula()
            peliculas.espereTecla()
        case "6":
            peliculas.borraCaracteristicaPelicula()
            peliculas.espereTecla()
        case "7":
            print("\n\t\t Terminaste la ejecución del Sistema ... Gracias ...")
            opcion = False
            peliculas.espereTecla()
        case _:
            print("\n\t\t Opción Invalida, intenta de nuevo ...")
            opcion = True