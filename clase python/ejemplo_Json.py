import json

fileProducts = open("productos.json")

products = json.load(fileProducts)
fileProducts.close

print(products,type(products))

newProduct = {
    "code": "P002",
    "name": "Product 2",
    "price": 2000,
    "active": True
}

products.append(newProduct)

prodSave = json.dumps(products)

print(prodSave,type(prodSave))

fileProducts = open("productos.json", "w")

fileProducts.write(prodSave)

fileProducts.close()


