# Escribir un programa para una empresa que tiene salas 
# de juegos para todas las edades y quiere calcular de 
# forma automática el precio que debe cobrar a sus clientes 
# por entrar. El programa debe preguntar al usuario la edad 
# del cliente y mostrar el precio de la entrada. Si el cliente 
# es menor de 4 año6s puede entrar gratis, 
# si tiene entre 4 y 18 años debe pagar Q5 y si es mayor de
# 18 años, Q10.


edad = int(input('Que edad tiene el cliente: '))
if edad <=4:
    print('Puede entrar gratis.')
elif edad >= 5 and edad <=18:
    print('Tendra que pagar Q5.00')
elif edad >=19:
    print('Tendra que pagar Q10.00')



