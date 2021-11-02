#Crear un programa que permite dar mantenimiento a un listado de alumnos 
#utilizando archivos, debe ser capaz de listar los alumnos, agregar nuevos
#y eliminar, al finalizar todas las operaciones debe guardar en un archivo
#llamado alumnos.txt.

import os

direccionamiento = (r'D:\Users\evant\Desktop\Escritorio 2.0\UNI\2DO SEMESTRE\ALGORITMOS\laboratorios\Laboratorio 3')

texto = 'Listado de Alumos'+'\n'
archivo = open(direccionamiento+'\\alumnos.txt','w')
archivo.write(texto)
archivo.close()

direccionamiento2 = (r'D:\Users\evant\Desktop\Escritorio 2.0\UNI\2DO SEMESTRE\ALGORITMOS\laboratorios\Laboratorio 3\\alumnos.txt')
archivos = int(input('¿Cuantas listas de alumnos desea crear?'))
for i in range(archivos):
    texto = 'Lisado de Alumnos #{}'.format(i+1)+'\n'
    alumnos = int(input('Ingrese el numero de alumnos a ingresar: '))
    for alumnosin in range(alumnos):
        nombrealumno = str(input('Ingrese el nombre del alumno: '))
        estudiantes = open(direccionamiento2,'a')
        estudiantes.write(nombrealumno + '\n')
        estudiantes.close()
    confirmacion = str(input('¿Quiere guardar el archivo? S/N: ').upper())
    if confirmacion == "S":
        print('Su archivo se guardó')
    elif confirmacion == 'N':
        print('Si no guarda se eliminara el archivo')
        confirmacion2 = str(input('¿Seguro quiere aliminar el archivo? S/N: ').upper())
        if confirmacion2 == "S":
            from os import remove
            remove(direccionamiento2)
            print('Se elimino exitosamente')
        else:
            print('Se canceló y guardó')



