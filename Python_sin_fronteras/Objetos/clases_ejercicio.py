# Sergio Garino Vargas 
# Fecha: 7/1/2023
# Este es un ejercicio de clases, crear una clase llamada 'Gato' que tenga 
# la propiedad de nombre y el sonido que hace un gato, también un metódo que
# utilice el sonido que hace el gato para imprimir el sonido que hace el gato,
# se debe hacer lo mismo para una clase llamada 'Perro'. Ambas clases deben ser
# instanciadas

class Gato:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    def saludo(self):
        print('Esta mascota se llama', self.nombre, 'y hace', self.sonido)

class Perro:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    def saludo(self):
        print('Esta mascota se llama', self.nombre, 'y hace', self.sonido)

gato_uno = Gato(nombre='Sol', sonido='Miau!')
gato_uno.saludo()


perro_uno = Perro(nombre='Doggy', sonido='Guau!')
perro_uno.saludo()