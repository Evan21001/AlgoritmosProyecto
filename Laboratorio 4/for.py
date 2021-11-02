print('for string')

mensaje = 'Un string es un objeto inmutable'

for letras in mensaje:
    print(letras)
print('\n','\n')

print('for lista')
numerospar = [2,4,6,8,10]
for numero in numerospar:
    print(numerospar)
print('\n','\n')

print('for diccionario')
usuario = {
    'nombre': 'Evan',
    'email': 'etejadad@miumg.edu.gt',
    'contraseña': 'oculta'
}

for llave, valor in usuario.items():
    print(llave,'-',valor)
    