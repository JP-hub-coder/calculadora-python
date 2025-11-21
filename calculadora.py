TerminarPrograma = False 

while(not TerminarPrograma):
    print("Calculadora")
    print("1.    Sumar")
    print("2.    Restar")
    print("3.    Multiplicar")
    print("4.    dividir")
    print("5.    SALIR")
    
    opcion = int(input("Que desea hacer?"))
    if opcion == 1:
        print("Sumar")
        n1 = int(input("Ingrese el primer número"))
        n2 = int(input("Ingrese el segundo número"))
        suma = n1 + n2
        print("Resultado: " + str(suma))
        input("\nPresione enter para continuar...")
    elif opcion == 2:
        print("Restar")
        n1 = int(input("Ingrese el primer número"))
        n2 = int(input("Ingrese el segundo número"))
        resta = n1 - n2
        print("Resultado: " + str(resta))
        input("\nPresione enter para continuar...")    
    elif opcion == 3:
        print("Multiplicar")
        n1 = int(input("Ingrese el primer número"))
        n2 = int(input("Ingrese el segundo número"))
        multiplicar = n1 * n2
        print("Resultado: " + str(multiplicar))
        input("\nPresione enter para continuar...")
    elif opcion == 4:
        print("Dividir")
        n1 = int(input("Ingrese el primer número"))
        n2 = int(input("Ingrese el segundo número"))
        if n2 == 0:
            print("Valor invalido")
        else:
             dividir = n1 / n2
             print("Resultado: " + str(dividir))
             input("\nPresione enter para continuar...")
    elif opcion == 5:
        print("Saliendo...")
        TerminarPrograma = True     
        
