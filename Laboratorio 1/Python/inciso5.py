# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas 
# a sus clientes. Los ingredientes para cada tipo de pizza aparecen a 
# continuación.
#•	Ingredientes vegetarianos: Pimiento y tofu.
#•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
#y en función de su respuesta le muestre un menú con los ingredientes disponibles 
#para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el
#tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si 
# la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

veganav = ('Vegana ')
normalv = ('Normal ')
incluyev = (' Mozzarella y Salsa de Tomate ')
ing1 = (' Pimiento')
ing2 = (' Tofu')
ing3 = (' Peperoni')
ing4 = (' Jamón')
ing5 = (' Salmón')

print('Le ofrecemos pizzas de dos tipos que son: ')
print('1. '+str(veganav))
print('2. '+str(normalv))

opcionelegida = int(input('Escoja el numero de pizza que desea: '))
if opcionelegida == 1:
    print('Tenemos los ingredientes para ofreserle:')
    print('1.1'+str(ing1))
    print('1.2'+str(ing2))
    vegana = float(input('Elija el numero del ingrediente: '))
    if vegana == 1.1:
        print('Su pizza es '+str(veganav)+'incluye:'+str(ing1)+','+str(incluyev))
    elif vegana == 1.2:
        print('Su pizza es '+str(veganav)+'incluye:'+str(ing2)+','+str(incluyev))
elif opcionelegida == 2:
    print('Tenemos los ingredientes para ofreserle:')
    print('2.1'+str(ing3))
    print('2.2'+str(ing4))
    print('2.3'+str(ing5))
    normal = float(input('Elija el numero del ingrediente: '))
    if normal == 2.1:
        print('Su pizza es '+str(normalv)+'incluye:'+str(ing3)+','+str(incluyev))
    elif normal == 2.2:
        print('Su pizza es '+str(normalv)+'incluye:'+str(ing4)+','+str(incluyev))
    elif normal == 2.3:
        print('Su pizza es '+str(normalv)+'incluye:'+str(ing5)+','+str(incluyev))