# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre
# por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el
# nombre del mes. (Sugerencia utilizar la función split la cual permite separar 
# un texto, por ejemplo "12-12".split("-") devolvera un arreglo con dos elementos 
# ["12", "12"] ).

import datetime

mydate = datetime.datetime.now()
mydate.strftime('%B')

print('Nuestra fecha y hora actual son: '+str(mydate))

meses = {
    1: 'Enero',
    2: 'Febreo',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre'
}
print('Escriba la fecha de la siguiente manera mm/dd/aaaa')
fechahoy = input('Escriba la fecha deseada: ')
fechaahora = fechahoy.split('/')
print(meses[int(fechaahora[0])],fechaahora[1],'del',fechaahora[2])
