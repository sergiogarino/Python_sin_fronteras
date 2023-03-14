# Sergio Garino Vargas 
# Fecha: 6/1/2023
# Orientación a objetos

# Clase creado con el método de 'self' para que esra sea genérica y que en cada
# instanciación sus propiedades sean definidas
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Así se crea un método:
    def saludo(self):
        print('Hola, mi nombre es', self.nombre, self.apellido)

# Instancio un objeto
usuario_uno = Usuario('Sergio', 'Garino')
usuario_dos = Usuario('Maricel', 'Vargas')

usuario_uno.saludo()
# Las propiedades de un objeto pueden modificarse y eliminarse
# Para modificar una propiedad
usuario_uno.nombre = 'Andrea'
usuario_uno.apellido = 'Cruz'

# Vuelo a utilizar el método .saludo del objeto usuario_uno
usuario_uno.saludo() 

# Para eliminar uso la palabra reservada del
del usuario_dos.apellido
usuario_dos.saludo()

# Output
# Hola, mi nombre es Sergio Garino
# Hola, mi nombre es Andrea Cruz
# Esto sale asi debido a que el propgrama dará error al imprimir una propiedad que no existe
# Traceback (most recent call last):
#   File "objetos4.py", line 31, in <module>
#     usuario_dos.saludo()
#   File "objetos4.py", line 14, in saludo
#     print('Hola, mi nombre es', self.nombre, self.apellido)
# AttributeError: 'Usuario' object has no attribute 'apellido'

