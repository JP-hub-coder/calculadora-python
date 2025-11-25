import os
opt = 0
productos = [{
               "code": "001",
               "name": "llantas",
               "price": "150000"
            },
            {
               "code": "002",
               "name": "Tapetes",
               "price": "50000"
            },
            {
               "code": "003",
               "name": "liquido de frenos",
               "price": "300000"
            }
            ]

def limpieza():
    input("Presione cualquier tecla para continuar...")
    os.system("clear")
    os.system("cls" if os.name == "nt" else "clear")

def productindex( code ):
    ind = -1
    for i in range(len(productos)):
        if productos[i]["code"] == code:
            ind = i
            break
    return ind        

while(True):
    print("1.  Agregar producto\n2. Modificar producto\n3. Limpiar diccionario")
    opt = int(input("\n¿Que desea hacer?>") or 0)
    match(opt):
        case 1:
            productos.append({
                "code": input("Escriba el código del producto: "),
                "name": input("Escriba el nombre del producto: "),
                "price": input("Escriba el precio del producto: "),
            })
            print("Producto agregado...")
        case 2:
            code = input("Código del producto a modificar: ")
            prodind = productindex(code)
            if prodind == -1:
                print(f"producto con código {code} no existe")
            else:
                print(f"Código: {productos[prodind].get('code')}")    
                print(f"nombre: {productos[prodind].get('name')}")    
                print(f"Precio: {productos[prodind].get('price')}")    
                print(f"Activo: {productos[prodind].get('active')}") 
        case 3:
            producto = {
               "code": "001",
               "name": "llantas",
               "price": "150000"
            }
            # producto.clear()
            items = producto.items()
            print(items)            
            for itm in items:
                print(itm)
            print(producto.keys())
            print(producto.values())
            keys = producto.keys()
            for k in keys:
                print(f"{k} {producto[k]}")
            
    limpieza()

    print(productos)
    if opt == 0:
        print("Bye")
        break
    

