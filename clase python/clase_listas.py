tupla = (1, 2, 3)
print(tupla)                               

tupla2 = "a", "b", "c"
print(tupla2)

# andicacion de tuplas
tupla3 = 1, 2, ('a', 'b'), 3
print (tupla3)

# Sacar valores de la tupla
print(tupla2[2])
print(tupla3[2][0])

#Convertir lista a tupla
lista = [1, "a", 2, "b", 3]
tupla4 = tuple(lista)
print(tupla4, type(tupla4))

#recorrer una tupla
for valor in tupla3:
    print(valor)

for i in range(len(tupla3)):
    print(tupla3[i])


#pasar el contenido de la tupla a otras variables

x, y, z = tupla
print(f"x={x}, y={y}, z={z}")


tupla5 = 1, 2, 5, 7, 5, 9, 5
print(tupla5.count(5)) 

print(tupla5.index(9))
print(tupla5.index(5, 3))