lenguajes = ['python','kotlin','java']

print (lenguajes)

#los arrays (lists) comienzan en la posicion 0
print (lenguajes[0])

lenguajes.sort() # esta funcion de lista ordena alfabeticamente
print(lenguajes)

#acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[2]}'
print(aprendiendo)

#Modificando valores de un arreglo
lenguajes[2] = 'php'
print (lenguajes)

#agregar elementos a un list o arreglo
lenguajes.append('ruby')
print(lenguajes)

#Eliminar a un arreglo (list)
del lenguajes[1]
print(lenguajes)

#Eliminar a un arreglo o list el ultimo elemento
lenguajes.pop ()
print(lenguajes)

#Eliminar con .pop una posicion en especifico
lenguajes.pop (0)
print (lenguajes)

#Eliminar por nombre
lenguajes.remove ('php')
print (lenguajes)

