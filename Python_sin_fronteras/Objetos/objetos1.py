# Sergio Garino Vargas 
# Fecha: 6/1/2023
# Orientación a objetos

# Es una convención poner los nombres de una clase iniciando con mayúscula
class Usuario:
    nombre = 'Sergio'
    apellido = 'Garino'

# Para generar una instancia es convención utilizar la primera letra en minúscula
# Una instacia es como un ejemplo de la clase que se haya creado
# Asi se instancia una clase
usuario_uno = Usuario()
print(Usuario)   # Output: <class '__main__.Usuario'>
print(usuario_uno)  # Output: <__main__.Usuario object at 0x7f8fe74b1eb0>
print(usuario_uno.nombre)  # Output: Sergio
print(usuario_uno.nombre, usuario_uno.apellido)  # Output: Sergio Garino
