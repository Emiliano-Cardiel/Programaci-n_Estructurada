import datos
from conexionBD import *

def CrearNota(id):
    res=True
    while True:
        datos.borrarPantalla()
        
        while True:
            try:
                datos.borrarPantalla()
                print("\n\t\t\t📝 ..::Crear una nota nueva::.. 📝\n")
                num = int(input("📞 Ingresa el número telefónico del cliente: "))
                cursor.execute("SELECT telefono FROM notas_clientes WHERE telefono = %s", (num,))
                resultado = cursor.fetchone()

                if resultado:
                    print("\n\t❌ Este número ya está registrado.")
                    datos.esperarTecla()
                    datos.borrarPantalla()
                    return
                else:
                    break
            except ValueError:
                datos.borrarPantalla()
                print("\n\t⚠️ Ingresa un número válido.")
                datos.esperarTecla()

        # Capturar datos
        res=True
        while res:
            datos.borrarPantalla()
            print("\n\t\t\t📝 ..::Crear una nota nueva::.. 📝\n")
            Nombre = input("👤 Nombre del cliente: ").upper().strip()
            res=datos.validar_len(Nombre)
            if res==False:
                break
            if res ==True:
                res=True
            

        res=True
        while res:
            print("\n\t\t\t📝 ..::Crear una nota nueva::.. 📝\n")
            Vehiculo = input("🚗 Modelo del vehículo: ").upper().strip()
            res=datos.validar_len(Vehiculo)
            if res==False:
                break
            if res ==True:
                res=True

        res=True
        while res:
            print("\n\t\t\t📝 ..::Crear una nota nueva::.. 📝\n")
            Anio = input("📅 Año del vehículo: ").strip()
            res=datos.validar_len(Anio)
            if res==False:
                break
            if res ==True:
                res=True

        res=True
        while res:
            print("\n\t\t\t📝 ..::Crear una nota nueva::.. 📝\n")
            Color = input("🎨 Color del vehículo: ").upper().strip()
            res=datos.validar_len(Color)
            if res==False:
                break
            if res ==True:
                res=True

        res=True
        while res:
            print("\n\t\t\t📝 ..::Crear una nota nueva::.. 📝\n")
            Comentario = input("📝 Comentario: ").upper().strip()
            res=datos.validar_len(Comentario)
            if res==False:
                break
            if res ==True:
                res=True

        print("=" * 50)
        print(f"Número telefónico: {num}📌 \nCliente: {Nombre}\n🚗 Vehículo: {Vehiculo} ({Anio}) - Color: {Color}\n📝 Comentario: {Comentario}")
        print("=" * 50)
        respuesta=input("\n ¿Estan correctos los datos?").lower().strip()
        if respuesta=="si":
                break
        if respuesta=="no":
            res=True

    cursor.execute("INSERT INTO notas_clientes (id_usuario, telefono, nombre, vehiculo, anio, color, comentario) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id, num, Nombre, Vehiculo, int(Anio), Color, Comentario))
    conexion.commit()

def BorrarNota(id_usuario):
    datos.borrarPantalla()
    print("\n\t\t\t🔴 ..::Borrar o quitar nota::.. 🔴\n")
    cursor.execute("SELECT * FROM notas_clientes WHERE id_usuario = %s", (id_usuario,))
    lista_clientes = cursor.fetchall()

    if len(lista_clientes) > 0:
        print(f"{'ID':<10} {'Telefono':<15} {'Nombre':<15} {'Vehiculo':<15} {'Año':<10} {'Color':<10} {'Comentario':<15}")
        print("-" * 100)
        for fila in lista_clientes:
            print(f"{fila[0]:<10} {fila[2]:<15} {fila[3]:<15} {fila[4]:<15} {fila[5]:<10} {fila[6]:<10} {fila[7]:<15}")
        print("-" * 100)

        resp = input("¿Deseas borrar alguna nota? (si/no): ").lower().strip()
        while resp not in ["si", "no"]:
            print("Ingrese una respuesta correcta (si/no)")
            resp = input("¿Deseas borrar alguna nota? (si/no): ").lower().strip()

        if resp == "si":
            ids_validos = [str(fila[0]) for fila in lista_clientes]
            while True:
                try:
                    nota_id = input("\t\t Ingresa la ID de la nota a eliminar: ").strip()
                    if nota_id in ids_validos:
                        confirmacion = input(f"¿Estás seguro de que deseas borrar la nota #{nota_id}? (si/no): ").lower().strip()
                        while confirmacion not in ["si", "no"]:
                            print("Respuesta inválida. Escribe 'si' o 'no'.")
                            confirmacion = input(f"¿Estás seguro de que deseas borrar la nota #{nota_id}? (si/no): ").lower().strip()

                        if confirmacion == "si":
                            cursor.execute("DELETE FROM notas_clientes WHERE id = %s", (nota_id,))
                            conexion.commit()
                            print(f"✅ Se borró la nota #{nota_id} con éxito.")
                        else:
                            print("❎ Operación cancelada. No se borró ninguna nota.")
                        break
                    else:
                        print("❌ No existe esta nota. Intenta con una ID válida.")
                except Exception as e:
                    print(f"⚠️ Error al intentar borrar la nota: {e}")
                    break
        else:
            print("No se borró ninguna nota.")
    else:
        print("📭 No hay notas para este usuario.")
            
def MostrarNotas(id_usuario):
    datos.borrarPantalla()
    print("\n\t\t\t👀..::Mostrar notas::..👀\n")
    cursor.execute("select * from notas_clientes where id_usuario=%s",(id_usuario,))
    lista_clientes=cursor.fetchall()
    if len(lista_clientes)>0:
        print(f"{"ID":<10} {"Telefono":<15} {"Nombre":<15} {"Vehiculo":<15} {"Año":<10} {"Color":<10} {"Comentario":<15}")
        print(f"-"*100)
        for fila in lista_clientes:
            print(f"{fila[0]:<10} {fila[2]:<15} {fila[3]:<15} {fila[4]:<15} {fila[5]:<10} {fila[6]:<10} {fila[7]:<15}")
        print(f"-"*100)
    else:
        print("No hay notas para este usuario")

def ModificarNota(id_usuario):
    datos.borrarPantalla()
    print("\n\t🔍 ..:: Buscar nota del cliente por número ::.. 🔍\n")
    cursor.execute("select * from notas_clientes where id_usuario=%s",(id_usuario,))
    lista_clientes=cursor.fetchall()
    if len(lista_clientes)>0:
        print(f"{"ID":<10} {"Telefono":<15} {"Nombre":<15} {"Vehiculo":<15} {"Año":<10} {"Color":<10} {"Comentario":<15}")
        print(f"-"*100)
        for fila in lista_clientes:
            print(f"{fila[0]:<10} {fila[2]:<15} {fila[3]:<15} {fila[4]:<15} {fila[5]:<10} {fila[6]:<10} {fila[7]:<15}")
        print(f"-"*100)
        resp=input("Deseas modificar alguna nota? (si/no) ").lower().strip()
        while resp!="si" and resp!="no":
            print("Ingrese una respuesta correcta (si/no)")
            resp=input("Deseas borrar alguna nota? (si/no)").lower().strip()
            if resp=="si" or resp=="no":
                break

        if resp=="si":
            ids_validos = [str(fila[0]) for fila in lista_clientes]
            while True:
                try:
                    print("\n\t.::Si no quieres modificar alguna característica, introduce los mismos datos::.\t")
                    id = input("\t\t ID de la nota a modificar: ")
                    if id in ids_validos:
                        telefono = input("\t Nuevo telefono: ").upper().strip()
                        nombre = input("\t Nuevo nombre: ").upper().strip()
                        vehiculo = input("\t Nuevo vehiculo: ").upper().strip()
                        anio = input("\t Nuevo año: ").upper().strip()
                        color = input("\t Nuevo color: ").upper().strip()
                        comentario = input("\t Nuevo comentario: ").upper().strip()
                        cursor.execute("update notas_clientes set telefono=%s, nombre=%s, vehiculo=%s, anio=%s, color=%s, comentario=%s where id=%s ",(telefono,nombre,vehiculo,anio,color,comentario,id))
                        conexion.commit()
                        res=True
                        break
                except Exception as e:
                    print(f"⚠️ Error al intentar borrar la nota: {id}")
                    break
                except:
                    res=False
            if res:
                print(f"\n\tSe modifico la nota #{id} con exito\t")
            else:
                print(f"No fue posible modificar la nota en este momento, intente de nuevo mas tarde") 
    else:
        print("No hay notas para este usuario")