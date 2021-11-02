#. Escribir un programa que dado un monto en quetzales y un divisa de destino, 
# realice la conversión sin utilizar estructuras de decisión (if-else, switch).
# Los tipos de cambio posibles son:
# 1 Euro = 9 Quetzales
# 1 Dolar = 7.7 Quetzales
# 1 Libra = 12 Quetzales
# 1 Peso = 0.4 Quetzales

monedasexistencia={
    'Euro': 9,
    'Dolar': 7.7,
    'Libra': 12,
    'Peso': 0.4
}
moneda=input('Ingrese el nombre de la moneda a la que desea convertir: ')
cantidad = float(input('Ingrese la cantidad que desea convertir a '+str(moneda)+': '))
if moneda in monedasexistencia:
    resultado = cantidad * monedasexistencia[moneda]
    print('El monto en '+str(moneda)+' es equivalente a: '+str(resultado)+' Quetzales')
else:
    print('La moneda '+str(moneda)+' no la podemos convertir a nuestra moneda')
