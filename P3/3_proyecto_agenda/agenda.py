import mysql.connector
from mysql.connector import Error
'''
contactos={
        "Ruben":["6181111111","ruben@gmail.com"]


}
'''


def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(f"\n\t\t\U0001F552 Oprima cualquier tecla pra continuar ...")

def menu_principal():
    print(F"\n\t\t\t\U0001F4DE Sistema de gestion de agenda de contactos  \U0001F4DE\n\n\t1\uFE0F\u20E3\tAgregar contacto \n\t2\uFE0F\u20E3\tMostrar todos los contactos\n\t3\uFE0F\u20E3\tBuscar contacto por nombre\n\t4\uFE0F\u20E3\tModificar atributo\n\t5\uFE0F\u20E3\tBorrar un contacto\n \t6\uFE0F\u20E3\tSalir")
    opcion=input(f"\t\t\U0001F4DD Elige una opcion (1-4): ").upper()
    return opcion

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_agenda"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None

def agregarContac(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\t\t Agregar contactos ")
        nombre=input("Ingrese su nombre: ").upper().strip()
        if nombre in agenda:
            print("Este contacto ya existe")
        else:
            telefono=input("Ingrese su numero de telefono: ").upper()
            email=input("Ingrese su correo electronico: ").lower().strip()
            agenda[nombre]=[telefono,email]
            cursor=conexionBD.cursor()
            sql="insert into agenda ( nombre, telefono, email) values ( %s, %s, %s)"
            for i in agenda:
                val=(i,agenda[i][0],agenda[i][1])
            cursor.execute(sql,val)
            conexionBD.commit()            
            print("Operacion realizada con exito")
        print("")


def mostrarContac(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      cursor=conexionBD.cursor()
      sql="select * from agenda"
      cursor.execute(sql)
      registros=cursor.fetchall()
      print("\t\t Mostrar contactos ")
      if registros:
        print(f"\t\t  {'Id':<10}{'Nombre':<15}{'Telefono':<15}{'E-mail':<10}")
        print("\t\t","-"*55)
        for fila in registros:
            print(f"\t\t  {fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<10}")
            print("\t\t","-"*55)  
      else:
        print("\n\t .:: No hay calificaciones en el Sistema ::. ")


def buscarContac(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      nombre=input("Dame el nombre del contacto a buscar: ").upper().strip()
      cursor=conexionBD.cursor()
      sql="select * from agenda where nombre=%s"
      val=(nombre,)
      cursor.execute(sql,val)
      registros=cursor.fetchall()
      if registros:
        print(f"\n\tMostrar las Contactos")
        print(f"\t {'Id':<10}{'Nombre':<15}{'Telefono':<15}{'E-mail':<10}")
        print("\t",f"-"*60)
        for fila in registros:
          print(f"\t {fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<10}")
        print("\t",f"-"*60)  
      else:
        print("\n\t .:: No hay peliculas en el Sistema con ese nombre::. ")

def modificarContac(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        nombre1=input("Dame el nombre del contacto a modificar: ").upper().strip()
        cursor=conexionBD.cursor()
        sql="select * from agenda where nombre=%s"
        val=(nombre1,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print(f"\n\tMostrar la Agenda")
            print(f"\t {'Id':<10}{'Nombre':<15}{'Telefono':<15}{'E-mail':<10}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
                print(f"-"*80) 
            resp=input(f"¿Deseas modificar el contacto {nombre1}? (Si/No): " ).lower().strip()
            if resp=="si":
                nombre=input("Ingrese su nuevo nombre: ").upper().strip()
                telefono=input("Ingrese su nuevo numero de telefono: ").upper()
                email=input("Ingrese su nuevo correo electronico: ").lower().strip()
                agenda[nombre]=[telefono,email]
                sql="update agenda set nombre=%s, telefono=%s, email=%s where nombre=%s"
                val=(nombre,telefono,email,nombre1)
                print(val)
                cursor.execute(sql,val)
                conexionBD.commit()
                print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::")
        else:
            print("\n\t .:: No hay peliculas en el Sistema con ese nombre::. ")
                
def borrarContac(agenda):
    borrarPantalla()
    print("\t\t Borrar contacto ")
    conexionBD=conectar()
    if conexionBD!=None:
        nombre=input("Dame el nombre del contacto a borrar: ").upper().strip()
        cursor=conexionBD.cursor()
        sql="select * from agenda where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
                print(f"\t {'Id':<10}{'Nombre':<15}{'Telefono':<15}{'E-mail':<10}")
                print(f"-"*80)
                for fila in registros:
                    print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
                    print(f"-"*80) 
                resp=input(f"¿Deseas borrar el contacto {nombre}? (Si/No): " ).lower().strip()
                if resp=="si":
                    sql="delete from agenda where nombre=%s"
                    val=(nombre,)
                    cursor.execute(sql,val)
                    conexionBD.commit()
                print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::")
        else:
            print("\n\t .:: No hay peliculas en el Sistema con ese nombre::. ")

            
                
                
