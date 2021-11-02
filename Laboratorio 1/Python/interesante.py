numeros = []
veces = int(input('Ingrese cuantos numeros desea comparar: '))
# Le agregue una variable 'veces' para que se imprima segun las veces que se pidan
# la idea del 'for' con un rango fue la que me sirvio para inciso 4 y 1
for i in range(veces):
  numero = float(input("Introduce el número #{}: ".format(i + 1)))
  numeros.append(numero)

# Asumir que el menor es el primero de la lista
menor = numeros[0]
# Recorrer y comparar
for numero in numeros:
    if numero < menor:
        menor = numero
# Imprimir el resultado
print("Menor:", menor)