#Escribir un programa que pregunte al usuario una cantidad a invertir,
#el interés anual y el número de años, y muestre por pantalla el capital 
#obtenido en la inversión cada año que dura la inversión.

resultado=[]
print('Nota: Escribir el interes anual sin el signo % y en numeros enteros')
invertir= int(input('Cantidad a invertir: '))
inanual = int(input('Interés anual: '))
anual = float(inanual / 100)
print('El interes aunual en decimales es: '+str(anual))
años = int(input('Numero de años: '))
print(anual)
resultadoecuacion = anual * invertir
for i in range(años):
  ecuacion = ("#{} año de interes anual: ".format(i + 1) + str(resultadoecuacion))
  resultado.append(ecuacion)
  print(ecuacion)
Totalinversion = resultadoecuacion * años
print('Total de iversion por los '+str(años)+' de interes: '+str(Totalinversion))
  