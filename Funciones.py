TerminarPrograma = False 

while(not TerminarPrograma):
    print("Calculadora")
    print("1.    Sumar")
    print("2.    Restar")
    print("3.    Multiplicar")
    print("4.    dividir")
    print("5.    SALIR")
    
    opcion = int(input("Que desea hacer?"))
    if opcion == 5:
        break
    
    n1 = int(input("Ingrese el primer número"))
    n2 = int(input("Ingrese el segundo número"))
    resultado = 0
    if opcion == 1:
        resultado= n1 + n2
    elif opcion == 2:
        resultado= n1 - n1  
    elif opcion == 3:
        resultado = n1 * n2
    elif opcion == 4:
        print("Dividir")
        resultado= n1 / n2
    print(f"El resultado es: {str(resultado)}")
    input("\nPresione cualquier tecla para continuar...")





SI
