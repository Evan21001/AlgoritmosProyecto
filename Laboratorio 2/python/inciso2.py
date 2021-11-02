# Escribir un programa que guarde en un diccionario los precios de las frutas 
# de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre 
# por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en
#  el diccionario debe mostrar un mensaje informando de ello.
# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70


diccionariodic={
    'Plátano': 1.35,
    'Manzana': 0.80,
    'Pera': 0.85,
    'Naranja': 0.70
}
print('Las existencias son: ')
print(diccionariodic)
fruta = input('Ingrese el nombre de su fruta: ')
kilos = float(input('Cuantos kilos de esta fruta quiere: '))
if fruta in diccionariodic:
    precio = diccionariodic[fruta]*kilos
    print('Son ',kilos,'kilos de ',fruta)
    print('El precio a pagar es: ',precio)
else:
    print('La fruta ',fruta,' no la tenemos en existencia')
