def menuplatillos():
    TerminarPrograma = False
    while not TerminarPrograma:
       
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
        elif opcion == 2:
            TotalGeneral += 12000
        elif opcion == 3:
            TotalGeneral += 18000    
    
def menuprincipal():
    TerminarPrograma = False
    while not TerminarPrograma:
        print("==============")
        print("OPCIONES")
        print("1.   platillos")
        print("2.   bebidas")
        print("3.   adicionales")
        print("0.   SALIR")
        opcion = int(input("Que desea ordenar?"))
    
        if opcion == 0:
            print("Saliendo...")
            break
        elif opcion == 1:
            menuplatillos()
        elif opcion == 2:
            menubebidas()
        elif opcion == 3:
            menuadicionales()
    
def menubebidas():
    TerminarPrograma = False
    while not TerminarPrograma:
       
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
        elif opcion == 2:
            TotalGeneral += 2500
        elif opcion == 3:
            TotalGeneral += 1500   
            
            
def menuadicionales():
    TerminarPrograma = False
    while not TerminarPrograma:
       
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
        elif opcion == 2:
            TotalGeneral += 7000
        elif opcion == 3:
            TotalGeneral += 8000
            
menuprincipal()