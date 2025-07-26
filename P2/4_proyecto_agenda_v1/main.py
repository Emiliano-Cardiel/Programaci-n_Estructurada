import agenda

def main():
    agenda_contactos = {}
    opcion=True

    while opcion:
        agenda.borrarPantalla()
        opcion=agenda.menuPrincipal()

        if opcion== "1":
            agenda.agregar_contacto(agenda_contactos)
            agenda.espereTecla()
        elif opcion== "2":                
            agenda.mostrar_contacto(agenda_contactos)
            agenda.espereTecla()
        elif opcion== "3": 
            agenda.buscar_contacto(agenda_contactos)
            agenda.espereTecla()
        elif opcion== "4": 
            agenda.modificar_contacto(agenda_contactos)
            agenda.espereTecla()
        elif opcion== "5": 
            agenda.eliminar_contacto(agenda_contactos)
            agenda.espereTecla()
        elif opcion== "6":                
            print("\n\t\t \U0001F6AATerminaste la ejecución del Sistema ... Gracias ...\U0001F6AA")
            opcion = False
        else:               
            print("\n\t\t \u274COpción Invalida, intenta de nuevo ...\u274C")
            opcion = True
            agenda.espereTecla()

if __name__=="__main__":
    main()