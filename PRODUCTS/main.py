
from utils.menu import menu
from jsonFileHandler import *
from utils.utilListas import *

PRODUCT_FILE_PATH= "./Database/products.json"
options = ("Añadir producto",
"Mostrar producto",
"Editar producto",
"Eliminar producto",
"Buscar producto",
"SALIR")

while True:
    choice = menu("G E S T I Ó N  D E  P R O D U C T O S", options)
    match choice:
        case 1:
            product = {
                "code": input("ingrese el código del producto: "),
                "name": input("ingrese el nombre del producto: "),
                "provider": input("Ingrese proveedor del producto: "),
                "price": (input("ingrese precio del producto: ")),
                "active": True,
            }
            
            dataProducts = readFile(PRODUCT_FILE_PATH)
            dataProducts.append(product)
            saveFile(PRODUCT_FILE_PATH, dataProducts)
        case 2:
            products = readFile(PRODUCT_FILE_PATH)
            if len(products) == 0:
                print("No hay productos registrados...")
            else:    
                print("=== P R O D U C T O S  R E G I S T R A D O S ===\n")
                print("= CÓDIGO  NOMBRE                PROVEEDOR          PRECIO   ESTADO =\n")
                for product in products:
                    print(f"  {product['code']:<6} {product['name']:<22}  {product['provider']:<12} {product['price']:<12} {'Activo' if product['active'] else f'inactivo':<12}") 
        case 3:
            productCode = input("Código del producto a editar: ")
            products = readFile(PRODUCT_FILE_PATH)
            info = findDictionary(products, "code", productCode)
            if len(info.keys()) == 0:
                print("código no encontrado...")
            else:
                editProd = {
                    "name": input("Nuevo nombre: ") or info["data"]["name"],
                    "provider": input("Nuevo proveedor: ") or info["data"]["provider"],
                    "price": input("Nuevo precio: ") or info["data"]["price"],
                    "active": False if input("Nuevo estado ([A]ctivo/[I]nactivo): ") =="I" else True or info ["data"]["price"]
                }
                print(editProd)
        case 4:
            productCode = input("Código del producto a eliminar: ")
            products = readFile(PRODUCT_FILE_PATH)
            info = findDictionary(products, "code", productCode)
            products.pop(info["data"]["index"])
            saveFile(PRODUCT_FILE_PATH, dataProducts)
            print(f"se ha elminado el producto {info['data']['code']} - {info['data']['name']}") 
        case 5:
            productCode = input("Código del producto a buscar: ")
            products = readFile(PRODUCT_FILE_PATH)
            info = findDictionary(products, "code", productCode)
            if len(info.keys()) == 0:
                print("código no encontrado...")
            else:
                print(">> DATOS DEL PRODUCTO <<")
                print(f"  CÓDIGO: {info['data']['code']}")
                print(f"  NOMBRE: {info['data']['name']}")
                print(f"  PRECIO: {info['data']['price']}")
                print(f"  PROVEEDOR: {info['data']['provider']}")
                if   "active" == False:
                    print("  ESTADO: Inactivo")
                else:
                    print("  ESTADO:  Activo")    
        case 6:
            print("Bye!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            break


