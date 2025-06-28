#Crear un objeto que permita almacenar los siguientes atributos:(nombre, categoria,
#  clasificacion, genero, idioma) de peliculas
# pelicula = {
#         "nombre":"",
#         "categoria":"",
#         "clasificacion":"",
#         "genero":"",
#         "idioma":"",
# }

pelicula={}

def borrarPantalla():
    import os
    os.system('cls')
    
def espereTecla():
    input("\n\t\t Presiona una tecla para continuar ...")

def crearPelicula():
    borrarPantalla()
    print("\n\t .::: Agregar Peliculas :::.\n") 
    pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
    #pelicula["nombre"]=input("Ingresa el nombre: ").upper().strip() Otra forma de hacer linea 23
    pelicula.update({"categoria":input("Ingresa la categoria: ").upper().strip()})
    pelicula.update({"clasificacion":input("Ingresa la clasificacion: ").upper().strip()})
    pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
    print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def mostrarPelicula():
    borrarPantalla()
    print("\n\t .:: Mostrar Peliculas ::.\n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i} : {pelicula[i]}")
    else:
        print("\n\t .:: No hay Peliculas en el Sistema ::.")

def borrarPelicula():
    borrarPantalla()
    print("\n\t .:: Borrar o Quitar la Pelicula ::.\n")
    if len(pelicula)>0:
        resp=input("¿Deseas borrar o quitar la pelicula? (Si/No) ").lower().strip()
        if resp=="si":
            pelicula.clear()
    else:
        print("\n\t .:: No hay Peliculas en el Sistema ::.")

def agregarCaracteristicaPelicula():
    borrarPantalla()
    print("\n\t .:: Agregar Característica a una Pelicula ::.\n")
    atributo=input("Ingresa el nombre de la nueva característica que deseas agregar: ").lower().strip()
    valor_atributo=input("Ingresa el valor de la nueva caracteristica que agregar: ").upper().strip()
    #pelicula.update({atributo:valor_atributo})
    pelicula[atributo]=valor_atributo
    print("\n\t\t ::: ¡LA OPERACION SE REALIZÓ CON EXITO! :::")

def modificarCaracteristicaPelicula():
    borrarPantalla()
    print("\n\t .:: Modificar Característica de una Pelicula ::. \n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\t{i} : {pelicula[i]}")
            resp=input(f"\n\t Desas modificar el valor de esta característica {i}?(Si/No) ").lower().strip()
            if resp =="si":
                val=input(f"\n\t Ingresa el nuevo valor de la Característica {i}: ").upper().strip()
                pelicula[i]= val
                #pelicula.update({i:val}) Modificar el valor de un atributo de un objeto (diccionario)
                print("\n\t\t ::: ¡LA OPERACION SE REALIZÓ CON EXITO! :::")
    else:
        print("\n\t .:: No hay Peliculas en el sistema ::.")

def borraCaracteristicaPelicula():
    borrarPantalla()
    print("\n\t .:: Borra la Característica de una Pelicula ::. \n")
    if len(pelicula)>0:
        print("\n\t Valores Actuales: ")
        for i in pelicula:
            print(f"\t{i} : {pelicula[i]}")
        resp=input(f"t\ ¿Deseas borrar alguna característica? (Si/No) ").lower().strip
        if resp=="si":
            elim=input(f"Ingresa la característica que desas borrar o quitar {i}: ")
            pelicula.pop({i:elim})
    else:
        print("\n\t .:: No hay Peliculas en el sistema ::.")
        # if len(pelicula)>0:
    #     for i in pelicula:
    #         print(f"\t{i} : {pelicula[i]}")
    #         resp=input(f"\n\t Desas modificar el valor de esta característica {i}?(Si/No) ").lower().strip()
    #         if resp =="si":
    #             val=input(f"\n\t Ingresa el nuevo valor de la Característica {i}: ").upper().strip()
    #             pelicula[i]= val
    #             #pelicula.update({i:val}) Modificar el valor de un atributo de un objeto (diccionario)
    #             print("\n\t\t ::: ¡LA OPERACION SE REALIZÓ CON EXITO! :::")