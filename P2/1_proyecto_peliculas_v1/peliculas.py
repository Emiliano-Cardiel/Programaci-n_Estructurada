peliculas = []

def borrarPantalla():
    import os
    os.system('cls')
def espereTecla():
    input("\n\t\t Presiona una tecla para continuar ...")

def agregarPeliculas():
    borrarPantalla()
    print("\n\t\t .::: AGREGAR PELICULAS :::.\n")
    peliculas.append(input("\t Ingresa el nombre de la pelicula: ").upper().strip())
    print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t .:: Mostrar Peliculas ::.\n")
    if len(peliculas) == 0:
        print("\n\t No hay peliculas en la lista.")
    else:
        print("\n\t Las peliculas son:")
        for i, pelicula in enumerate(peliculas, start=1):
            print(f"\t {i}. {pelicula}")
    print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")


def limpiarPeliculas():
    borrarPantalla()
    print("\n\t .:: Limpiar o borrar TODAS las peliculas ::.\n")
    resp = input("\t ¿Estas seguro de limpiar TODAS las peliculas? (Si/No): ").lower().strip()
    while resp != "si" and resp != "no":
        resp = input("\t Respuesta invalida, ingresa 'Si' o 'No': ").lower().strip()
    if resp == "si":
        print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")
        peliculas.clear()
    else:
        print("\n\t\t ::: ¡LA OPERACION NO SE REALIZO! :::")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t .:: Buscar Peliculas ::.\n")
    pelicula_buscar = input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print(f"\n\t La pelicula '{pelicula_buscar}' no se encuentra en la lista.")
    else:
        encontro=0  
        for i in range(0, len(peliculas)):
            if pelicula_buscar == peliculas[i]:
                print(f"\n\t La pelicula '{pelicula_buscar}' se encuentró en el casillero: {i+1}.")
                encontro+=1
        print(f"\n\t Tenemos {encontro} película(s) con ese titulo.")
        print("\n\t\t ::: ¡LA OPERACION SE REALIZÓ CON EXITO! :::")

def modificarPeliculas():
    borrarPantalla()
    print("\n\t .:: Modificar Peliculas ::.\n")
    pelicula_buscar = input("Ingrese el nombre de la pelicula a modificar: ").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
        print(f"\n\t La pelicula '{pelicula_buscar}' no se encuentra en la lista.")
    else:
        for i in range(0, len(peliculas)):
            if pelicula_buscar == peliculas[i]:
                resp=input(f"¿Desea actualizar la pelicula? (Si/No): ").lower()
                if resp == "si":
                    peliculas[i] = input("Ingrese el nuevo nombre de la pelicula: ").lower().strip()
                    encontro+=1
                    print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")
            
        print(f"\nSe modificó {encontro} pelicula(s) con este titulo.")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t .:: Borrar Peliculas ::.\n")
    pelicula_buscar = input("Ingrese el nombre de la pelicula a borrar: ").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
        print(f"\n\t La pelicula '{pelicula_buscar}' no se encuentra en la lista.")
    else:
        for i in range(0, len(peliculas)):
            while pelicula_buscar == peliculas[i]:
                resp=input(f"¿Desea quitar o borrar la pelicula del sistema? (Si/No): ").lower()
                if resp == "si":
                    peliculas.remove(i)
                    encontro+=1
                    print(f"\nLa pelicula que se borro es: {pelicula_buscar} y estaba en la casilla: {encontro}")
                    print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")
                else:
                    print("\nLa pelicula no se borrará")
        print(f"\nSe borraron {encontro} pelicula(s) con este titulo.")