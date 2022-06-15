diccionario=dict()
diccionario2=dict()
def ingreso():
    usuario=input("Introduce un usuario: ")
    contraseña=input("Introduce una contraseña: ")
    contraseña2=input("Introduce contraseña nuevamente: ")
    if contraseña==contraseña2:
        diccionario[usuario]=contraseña
    else:
        print("Las contraseñas no coinciden")
    aplicacion=input("Introduce una aplicación: ")
    diccionario2[usuario]=aplicacion

ingreso()
print(diccionario2)
