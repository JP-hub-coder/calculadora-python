import os
def limpieza():
    input("Presione cualquier tecla para continuar...")
    os.system("clear")
    os.system("cls" if os.name == "nt" else "clear")

TotalGeneral = 0
pedido = []

Tupla = ('Carne Asada - 18000', 'Higado - 12000', 'Pastas - 18000'),
('Pepsi - 2000', 'Coca Cola - 2500', 'Colombiana - 1500'),
('Papas Fritas - 5000', 'Ensalada - 7000', 'Yuca Frita - 8000')


def menuplatillos():
    global TotalGeneral
    TerminarPrograma = False
    while not TerminarPrograma:
        limpieza()
        print("=============================")
        print("======MENU DE PLATILLOS======")
        print("1.  Carne Asada  18000")
        print("2.  Higado       12000")
        print("3.  Pastas       18000")
        print("0.  SALIR")
        print("=============================")
        opcion = int(input("Que desea ordenar?"))    
        if opcion == 0:
            print("Saliendo...")
            break
        elif opcion == 1:
            TotalGeneral += 18000
            pedido.append (Tupla[0][0])
            print(f"valor actual: {TotalGeneral}")
        elif opcion == 2:
            TotalGeneral += 12000
            pedido.append (Tupla[0][1])
            print(f"valor actual: {TotalGeneral}")
        elif opcion == 3:
            TotalGeneral += 18000 
            pedido.append (Tupla[0][2])
            print(f"valor actual: {TotalGeneral}")   
    
def menuprincipal():
    global TotalGeneral
    TerminarPrograma = False
    while not TerminarPrograma:
        limpieza()
        print("==============")
        print("OPCIONES")
        print("1.   platillos")
        print("2.   bebidas")
        print("3.   adicionales")
        print("0.   SALIR")
        opcion = int(input("Que desea ordenar?"))
    
        if opcion == 0:
            print("Gracias por su compra")
            print("=======PEDIDO=======")
            for pedidos in pedido:
                print(pedidos)    
            print("====================")    
            print(f"Total final: {TotalGeneral}")
            print("Saliendo...")
            break
        elif opcion == 1:
            menuplatillos()
        elif opcion == 2:
            menubebidas()
        elif opcion == 3:
            menuadicionales()
    
def menubebidas():
    global TotalGeneral
    TerminarPrograma = False
    while not TerminarPrograma:
        limpieza()
        print("=============================")
        print("======MENU DE BEBIDAS======")
        print("1.  Pepsi           2000")
        print("2.  Coca Cola       2500")
        print("3.  Colombiana      1500")
        print("0.  SALIR")
        print("=============================")
        opcion = int(input("Que desea ordenar?"))    
        if opcion == 0:
            print("Saliendo...")
            break
        elif opcion == 1:
            TotalGeneral += 2000
            pedido.append (Tupla[1][0])
            print(f"valor actual: {TotalGeneral}")
        elif opcion == 2:
            TotalGeneral += 2500
            pedido.append (Tupla[1][1])
            print(f"valor actual: {TotalGeneral}")
        elif opcion == 3:
            TotalGeneral += 1500  
            pedido.append (Tupla[1][2])
            print(f"valor actual: {TotalGeneral}") 
            
            
def menuadicionales():
    global TotalGeneral
    TerminarPrograma = False
    while not TerminarPrograma:
        limpieza()
        print("=============================")
        print("=====MENU DE ADICIONALES=====")
        print("1.  Papas Fritas   5000")
        print("2.  Ensalada       7000")
        print("3.  Yuca Frita     8000")
        print("0.  SALIR")
        print("=============================")
        opcion = int(input("Que desea ordenar?"))    
        if opcion == 0:
            print("Saliendo...")
            break
        elif opcion == 1:
            TotalGeneral += 5000
            pedido.append (Tupla[2][0])
            print(f"valor actual: {TotalGeneral}")
        elif opcion == 2:
            TotalGeneral += 7000
            pedido.append (Tupla[2][1])
            print(f"valor actual: {TotalGeneral}")
        elif opcion == 3:
            TotalGeneral += 8000
            pedido.append (Tupla[2][2])
            print(f"valor actual: {TotalGeneral}")
            
menuprincipal()