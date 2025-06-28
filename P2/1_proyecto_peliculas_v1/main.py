'''
Crear un proyecto que permita gestionar (administrar) peliculas. 
Colocar un menu de opciones: Agregar, Borrar, Modificar, Mostrar,
Limpiar una lista de peliculas.

Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar listas para almacenar los nombres de las peliculas
'''

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t .::: GESTION DE PELICULAS :::.\n\n\t 1.-Agregar " \
    "\n\t 2.-Borrar \n\t 3.-Modificar " \
    "\n\t 4.-Mostrar \n\t 5.-Buscar " \
    "\n\t 6.-Limpiar \n\t 7.-Salir")
    opcion = input("\n\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.espereTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case "3":
            peliculas.modificarPeliculas()
            peliculas.espereTecla()
        case "4":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.espereTecla()
        case "6":
            peliculas.limpiarPeliculas()
            peliculas.espereTecla()
        case "7":
            print("\n\t\t Terminaste la ejecución del Sistema ... Gracias ...")
            opcion = False
            peliculas.espereTecla()
        case _:
            print("\n\t\t Opción Invalida, intenta de nuevo ...")
            opcion = True