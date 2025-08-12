from conexionBD import *
import getpass
from usuarios import usuario

def borrarPantalla():
    import os
    os.system("cls")
    
def esperarTecla():
    input("\n\t\t ..:: Oprima la tecla ENTER para continuar ::..")

def validar_len(variable):
        borrarPantalla()
        if len(variable)==0:
            print("El valor no puede estar vacio, ingrese nuevmente lo solicitado:")
            return True
        else:
            return False

def login():
    borrarPantalla()
    while True:
        borrarPantalla()
        print("\n \t.:: Sistema de Gestión de Clientes ::..\n\t\t1.- Registro\n\t\t2.- Login\n\t\t3.- Salir")
        opcion = input("\t\t Elige una opción: ").upper().strip()

        if opcion == "1" or opcion == "REGISTRO":
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            res=True
            while res:
                nombre = input("\t ¿Cuál es tu nombre?: ").upper().strip()
                res=validar_len(nombre)
                if res==False:
                    break
                if res ==True:
                    res=True

            res=True
            while res:
                apellidos = input("\t ¿Cuáles son tus apellidos?: ").upper().strip()
                res=validar_len(apellidos)
                if res==False:
                    break
                if res ==True:
                    res=True

            res=True
            while res:
                email = input("\t Ingresa tu email: ").lower().strip()
                res=validar_len(email)
                if res==False:
                    break
                if res ==True:
                    res=True

            res=True
            while res:
                password = getpass.getpass("\t Ingresa tu contraseña: ").strip()
                res=validar_len(password)
                if res==False:
                    break
                if res ==True:
                    res=True

            resultado = usuario.registrar(nombre, apellidos, email, password)
            if resultado:
                print(f"Se registró el usuario {nombre} {apellidos} correctamente")
            else:
                print("No fue posible registrar el usuario en este momento, inténtelo más tarde")
            esperarTecla()

        elif opcion == "2" or opcion == "LOGIN":
            while True:
                try:
                    borrarPantalla()
                    print("\n \t ..:: Inicio de Sesión ::..")
                    res=True
                    while res:
                        email = input("\t Ingresa tu E-mail: ").lower().strip()
                        res=validar_len(email)
                        if res==False:
                            break
                        if res ==True:
                            res=True
                    res=True
                    while res:
                        password = getpass.getpass("\t Ingresa tu contraseña: ").strip()
                        res=validar_len(password)
                        if res==False:
                            break
                        if res ==True:
                            res=True
                    lista_usuario = usuario.inicio_sesion(email, password)
                    if len(lista_usuario) > 0:
                        print("Inicio de sesión exitoso")
                        esperarTecla()
                        return lista_usuario[0]  # ← Devuelve el ID del usuario
                    else:
                        print("Verifique su usuario")
                        esperarTecla()
                except TypeError:
                    borrarPantalla()
                    print("Ingrese un correo y contraseña validos!")
                    esperarTecla()
        elif opcion == "3" or opcion == "SALIR":
                print("\n\tTerminó la ejecución del sistema")
                return None  # ← Usuario eligió salir

        else:
                print("Opción no válida")
                esperarTecla()

def menu():
    print(F"\n\t\t🗒️ .:::Notas  cliente:::. 🗒️\n\n\t1.-Crear nota  📝\n\t2.-Borrar nota  🔴\n\t3.-Mostrar notas  👀\n\t4.-Modificar nota  🛠️\n\t5.-Exportar a Excel  📊\n\t6.-Salir  📤")
    opcion=input(f"\t\t  Elige una opcion  ☝️ :").upper()
    return opcion

def exportExcel():
    import pandas as pd
    conexionBD_=conexion
    if conexionBD_!=None:
        df=pd.read_sql_query("select * from notas_clientes", conexionBD_)
        df.to_excel("Tabla_Notas_Clientes.xlsx", index=False)
        borrarPantalla()
        print("Datos exportados a Tabla_Notas_Clientes.xlsx")
    else:
        print("\n\t.::No se puede conectar a la base de datos::.\n")
