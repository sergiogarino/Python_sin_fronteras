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

usuario_uno = Usuario('Sergio', 'Garino')
usuario_dos = Usuario('Maricel', 'Vargas')

print(usuario_uno.nombre, usuario_uno.apellido) # Output: Sergio Garino
print(usuario_dos.nombre) # Output: Maricel
print(usuario_dos.apellido) # Output: Vargas



    