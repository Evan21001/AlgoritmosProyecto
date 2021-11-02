edad = input('Ingresa tu edad: ')
edad=int(edad)

if edad >= 18 and edad <=59:
    print('Usted es mayor de edad')
elif edad >= 60:
    print('Usted es una persona madura')
else:
    print('Usted no es mayor de edad')