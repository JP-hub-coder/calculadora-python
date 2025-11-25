# se define pasando un objeto iterable 
# como argumento(listas, tuplas, etc)

#conjunto = set([1, 8, 15, 5, 8, 9])


#dicc = set((1, 5, 6, 8, 1, 9))

#print( 2 in dicc)

#diccionario2 = set((1, 10, 8, 2))
#unir diccionarios

#diccresult = dicc.union(diccionario2)

#print (diccresult)

#diccresult = dicc | diccionario2

#print(diccresult)

#añadir elementos
#diccresult.add(10)
#diccresult.add(30)
#print(diccresult)

#diccresult.remove(1)
#print (diccresult)

#diccresult.discard(50)
#print(diccresult)

#diccresult.pop()
#print(diccresult)



  #     case 2:
   #         posición = int(input("posición del producto: "))   
    #        print(f"Producto a editar: {productos[posición]}")
     #       productos[posición] = input("Nuevo producto: ")
      #      print("producto editado")
       # case 3:
        #    print(f"productos registrados: {len(productos)}")
  #      case 4:
   #         posc = int(input("¿En que posición va a poner el nuevo producto?"))
    #        prod = input("Nombre del producto: ")
     #       productos.insert(posc, prod)
      #      print("Producto insertado")
       # case 5:
  #          otrosprod = ["Detergente", True, 5000,["campus", "Trainer"] ]
   #         productos.extend(otrosprod)    
    #        print("lista extendida...")
     #   case 6:
      #      prod = input("Elemento a eliminar: ")
  #          productos.remove(prod)
   #         print("Producto eliminado")
    #    case 7:
     #       posc = int(input("Posición del producto a elminar: "))
      #      print(f"Elemento eliminado {productos.pop(posc)}")
       # case 8:
  #          prod = input("Nombre del producto: ")
   #         print(f"El producto {prod} se repite {productos.count(prod)} veces")
    #    case 9:
     #       productos.sort()
      #      print("Productos ordenados...")
       # case 10:
        #    productos.reverse()
        #    print("Lista de productos invertida...")
        #case 11:
        #    productos.clear()
        #    print("lista vacia")


diccionario2 = dict(
        nombre = "jhon",
        edad = 28,
        esEstudiante = False
)

print(diccionario2)


print(diccionario2["nombre"])
print(diccionario2.get("nombre"))