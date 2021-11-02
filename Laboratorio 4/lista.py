numeros = [1,2,3,4,5,6,7,8,9,10]

numeros.append(11)
numeros.insert(0,0)
numeros.remove(5)
print(numeros)

numeros[2] = -50
primerosnumeros = numeros [0:4]
segundosnumeros = numeros [:: -1]

print('Los nuemeros que estan en la sub lista son: ',primerosnumeros)
print('Los nuevos que estan en la segunda sub lista son: ',segundosnumeros)
numeros.sort(reverse=True)
print(numeros)