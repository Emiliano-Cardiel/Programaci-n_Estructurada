def borrarPantalla():
    import os
    os.system('cls')
    
def espereTecla():
    input("\n\t\t \U0001F552Presiona una tecla para continuar ...\U0001F552")

def menuPrincipal():
    print("\n\t 📅.::: SISTEMA DE GESTIÓN DE AGENDA DE CONTACTOS :::.📅\n\n\t\t 1️⃣ Agregar Contacto "
"\n\t\t 2️⃣ Mostrar Todos los Contactos \n\t\t 3️⃣ Buscar Contacto por Nombre" 
"\n\t\t 4️⃣-Modificar Contacto por Nombre"  "\n\t\t 5️⃣-Eliminar Contacto" "\n\t\t 6️⃣ Salir")
    opcion = input("\n\t 👉Elige una opción (1-4): ").upper()
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\U0001F464..: AGREGAR CONTACTOS :..\U0001F464\n")
    nombre=input("Nombre del Contacto: ").upper().strip()
    if nombre in agenda:
        print("\n\tEste Contacto Ya Existe\n")
    else:
        tel=input("Teléfono del Contacto: ").upper().strip()
        email=input("Correo del Contacto: ").lower().strip()
        agenda[nombre]=[tel,email]
        print("\n\t\tAcción Realizada con Éxito\n")

def mostrar_contacto(agenda):
    borrarPantalla()
    print("\n\t\U0001F4DD..: MOSTRAR CONTACTOS :..\U0001F4DD\n")
    if not agenda:
        print("\n\tNo hay Contactos en la Agenda\n")
    else:
        print(f"{"NOMBRE":<15} {"TELEFONO":<15} {"E-MAIL":<10}")
        print(f"-"*60)
        for nombre,datos in agenda.items():
            print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<10}")
        print(f"-"*60)

def buscar_contacto(agenda):
    borrarPantalla()
    print("\n\t\U0001F4DD..: BUSCAR CONTACTOS :..\U0001F4DD\n")
    if not agenda:
        print("\n\tNo hay Contactos en la Agenda\n")
    else:
        nombre=input("Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"{"NOMBRE":<15} {"TELEFONO":<15} {"E-MAIL":<10}")
            print(f"-"*60)
            print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<10}")
            print(f"-"*60)
        else:
            print("Este contacto no existe")

def modificar_contacto(agenda):
    borrarPantalla()
    print("\n\t\U0001F4DD..: MODIFICAR CONTACTOS :..\U0001F4DD\n")
    if not agenda:
        print("\n\tNo hay Contactos en la Agenda\n")
    else:
        nombre=input("Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"NOMBRE: {nombre}\nTELÉFONO:{agenda[nombre][0]}\nE-mail:{agenda[nombre][1]}")
            resp=input("¿Deseas cambiar los valores? (Si/No)").lower().strip()
            if resp=="si":
                tel=input("Teléfono del Contacto: ").upper().strip()
                email=input("Correo del Contacto: ").lower().strip()
                agenda[nombre]=[tel,email]
                print("\n\t\tAcción Realizada con Éxito\n")
        else:
            print("Este contacto no existe")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("\n\t\U0001F4DD..: ELIMINAR CONTACTOS :..\U0001F4DD\n")
    if not agenda:
        print("\n\tNo hay Contactos en la Agenda\n")
    else:
        nombre=input("Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"NOMBRE: {nombre}\nTELÉFONO:{agenda[nombre][0]}\nE-mail:{agenda[nombre][1]}")
            resp=input("¿Deseas eliminar los valores? (Si/No)").lower().strip()
            if resp=="si":
                agenda.pop(nombre)
                print("Contacto Borrado Correctamente")
            else:
                print("Lo contactos permanecieron intactos")
        else:
            print("Este contacto no existe")

