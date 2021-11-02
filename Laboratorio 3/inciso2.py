# Crear programa que dada una carpeta organice todos los archivos en subcarpetas basados en su tipo en 3 carpetas:
# 1. Imagenes (.jpg, .jpeg, .png)
# 2. Documentos (.pdf, .xlsx, .docx)
# 3. Musica (.mp3)


import os
import shutil
direccionamiento = (r'D:\Users\evant\Desktop\Escritorio 2.0\UNI\2DO SEMESTRE\ALGORITMOS\laboratorios\Laboratorio 3')
confirmacion = str(input('¿Quiere ordenar sus archivos? S/N \n'))
if confirmacion == 'S':
    shutil.move(direccionamiento + '\\doc.docx', direccionamiento +'\\DOC\\doc.docx')
    shutil.move(direccionamiento + '\\imagen.jpg', direccionamiento +'\\JPG\\imagen.jpg')
    shutil.move(direccionamiento + '\\musica.mp3', direccionamiento +'\\MP3\\musica.mp3')
else:
    print('No se ordenarán los archivos')
