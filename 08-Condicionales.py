#Revisar si una condicion es mayor a
balance = 500
if balance > 0:
    print('Puedes pagar')

else:
    print ('No tiene Saldo')

#Likes
likes = 200
if likes == 200:
    print ('Excelente, 200 Likes')

#If con texto
lenguaje = 'Python'
if lenguaje == 'Python':
    print('Excelente decision')

#Evaluar un boolean
usuario_autenticado = True

if usuario_autenticado:
    print('Acceso al Sistema')
else:
    print('Debes Iniciar Sesion')

#Evaluar un Elemento de una lista
lenguajes = ['python','kotlin','java','Javascript','ruby','go' ]
if 'php' in lenguajes:
    print('php Si existe')
else:
    print ('No no esta en la lista')

#if anidados
usuario_autenticado = True
usuario_admin = False

if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
    print('Acceso al Sistema')
else:
    print('Debes Iniciar Sesion')


