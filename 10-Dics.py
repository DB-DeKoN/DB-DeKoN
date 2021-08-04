#Creando diccionario Simple
cancion = { 
    'artista' : 'metalica', #Llave y Valor
    'cancion' : 'Enter Sandman',
    'lanzamiento': 1992,
    'likes': 3000
}

#Acceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])

#Mezclar con un string
artista = cancion ['artista']


print(f'Estoy eescuchando a {artista}')

#Agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'
print(cancion)

#Reemplazar Valor existente
cancion['cancion'] = 'Seek and Destroy'
print(cancion)

#Eliminar un Valor
del cancion ['lanzamiento']
print(cancion)