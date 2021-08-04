#Iniciar un diccionario vacio
jugador = {}
print(jugador)

#Se une un jugador
jugador['nombre'] = 'juan'
jugador['puntaje'] = 0
print(jugador)

#Incrementa su puntaje
jugador['puntaje'] = 100
print(jugador)

#Incrementa su puntaje
jugador['puntaje'] = 200
print(jugador)

#Acceder a un valor
print(jugador.get('consola', 'No existe ese valor'))

#Iterar en el Diccionario
for llave, valor in jugador.items():
    print(llave)
    print(valor)

#Eliminarjugador y puntaje
del jugador['puntaje']
del jugador['nombre']
print(jugador)