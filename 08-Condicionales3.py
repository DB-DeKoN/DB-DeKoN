#Operadores and y or

usuario_logueado = True
usuario_admin = False
if usuario_logueado and usuario_admin:
    print('administrador')
elif usuario_logueado:
    print('Acceso al Sistema')
else:
    print('Debes Iniciar Sesion')