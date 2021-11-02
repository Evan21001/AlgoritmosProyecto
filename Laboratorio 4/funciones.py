print('funciones con datos de tipo string')

def saludar (username):
    print('hola '+username)

saludar('Evan Duarte')
print('\n')

print('functiones con suma')
def suma (numero_uno, numero_dos):
    return numero_uno + numero_dos
resultado = suma (50,20)
print(resultado)
print('\n')

print('function con n parametros')
def usuarios (**kwargs):
    print(kwargs)
usuarios(nombre='Evan', edad= 18)

print('\n')