

def menu(title, options):
    choice = 0
    index = 1
    print("===========================================|")
    print("== G E S T I Ó N  D E  P R O D U C T O S ==|")
    print("===========================================|")
    print("==                                         |") 
    for item in options:
        print(f"{index}, {item}")
        index += 1

    while True:    
        try:
            choice = int(input("-->¿Que desea hacer?: "))
            if choice not in range(1, len(options)+1):
                print("--> Chino pendejo aprenda a contar")
            else: 
                break
        except ValueError:
            print("Solo puede digitar numeros")    
    return choice









