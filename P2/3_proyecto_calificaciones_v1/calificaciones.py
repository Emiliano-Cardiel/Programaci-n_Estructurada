# lista=[
#         ["Ruben",10.0,10.0,10.0],
#         ["Andres",8.0,9.5,6.8]
#     ]

def borrarPantalla():
    import os
    os.system('cls')
    
def espereTecla():
    input("\n\t\t \U0001F552Presiona una tecla para continuar ...\U0001F552")

def menuPrincipal():
    print("\n\t\t \U0001F4DD.::: SISTEMA DE GESTION DE CALIFICACIONES :::.\U0001F4DD\n\n\t 1️⃣ Agregar " \
    "\n\t 2️⃣ Mostrar \n\t 3️⃣ Calcular Promedios " "\n\t 4️⃣-Salir")
    opcion = input("\n\t Elige una opción (1-4): ").upper()
    return opcion

def agregar_calif(lista):
    borrarPantalla()
    print("\n\t\U0001F4DD..: AGREGAR CALIFICACIONES :..\U0001F4DD\n")
    nombre=input("\U0001F464Nombre del Alumno: ").upper().strip()
    calificaciones=[]
    for i in range (1,4):
        continua=True
        while continua:
            try:
                cal=(float(input(f"\U0001F50DCalificacion #{i}: ")))
                if cal>=0 and cal<=10:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("\n\t\u274C...Ingresa un valor comprendido entre el 0 y 10\u274C\n")    
            except ValueError:
                print("\n\t \u274C::: Ingresa un valor numerico :::\u274C\n")
                espereTecla()  
    lista.append([nombre]+calificaciones)
    print("\n\t\t \u2705::: ¡LA ACCIÓN SE REALIZO CON ÉXITO! :::\u2705\n") 

def mostrar_calif(lista):
    borrarPantalla()
    print("\n\t\U0001F4DD..: MOSTRAR CALIFICACIONES :..\U0001F4DD\n")
    if len(lista)>0:
        print(f"{'Nombre':<15}{'Calif. 1':<10}{'Calif.2':<10}{'Calif.3':<10}")
        print("-"*50)
        for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print("-"*50)
        cuantos=len(lista)
        print(f"Son {cuantos} alumno(s)")
    else:
        print("\n\t \u26A0::: No hay Calificaciones en el Sistema :::\u26A0\n")
        espereTecla()
    print("\n\t\t \u2705::: ¡LA ACCIÓN SE REALIZO CON ÉXITO! :::\u2705\n") 

def calcular_prom_calif(lista):
    borrarPantalla()
    print("\n\t\U0001F4DD..: PROMEDIO DE ALUMNOS :..\U0001F4DD\n")
    if len(lista)>0:
        print(f"{'Nombre':<15}{'Promedio':<10}")
        print("-"*40)
        promedio_grupal=0
        for fila in lista:
           nombre=fila[0]
           promedio=(fila[1]+fila[2]+fila[3])/3
        #    promedio=sum(fila[1:])/3 Forma de hacerlo (factorial)
           print(f"{nombre:<15}{promedio:.2f}")
           promedio_grupal+=promedio
        print("-"*40)
        promedio_grupal=promedio_grupal/len(lista)
        print(f"\U0001F389El Promedio del Grupo es: {promedio_grupal:.2f}\U0001F389 ")
    else:
        print("\u26A0\n\t ::: No hay Calificaciones en el Sistema :::\u26A0\n")
        espereTecla()
    print("\n\t \u2705::: ¡LA ACCIÓN SE REALIZO CON ÉXITO! :::\u2705\n") 