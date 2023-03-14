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

# Accediendo a un método
usuario_uno.saludo()  
usuario_dos.saludo()

# Output
# Hola, mi nombre es Sergio Garino
# Hola, mi nombre es Maricel Vargas