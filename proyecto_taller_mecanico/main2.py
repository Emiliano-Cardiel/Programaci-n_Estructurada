import datos
from clientes import cliente
 
while True:
    datos.borrarPantalla()
    id_usuario = datos.login()

    if id_usuario is not None:
        while True:
            datos.borrarPantalla()
            opcion = datos.menu()
            match opcion:
                case "1":
                    cliente.CrearNota(id_usuario)
                    datos.esperarTecla()
                case "2":
                    cliente.BorrarNota(id_usuario)
                    datos.esperarTecla()
                case "3":
                    cliente.MostrarNotas(id_usuario)
                    datos.esperarTecla()
                case "4":
                    cliente.ModificarNota(id_usuario)
                    datos.esperarTecla()
                case "5":
                    datos.exportExcel()
                    datos.esperarTecla()
                case "6":
                    break
                case _:
                    print("Operación no válida")
                    datos.esperarTecla()
    else:
        break