# Sergio Garino Vargas 
# Fecha: 7/1/2023
# Ejercicio de herencia, crear una clase llama 'Animal', la cual tiene las
# propiedades de nombre y un sonido que hace ese animal. 
# También crear las clases de 'Gato' y 'Perro' las cuales herendan las 
# propiedades de la clase 'Animal' e implementan un método el cual utiliza la 
# propiedad del sonido que hace el animal para saludar

class Animal:
    def __init__(self, nombre_del_animal, sonido_que_hace):
        self.nombre = nombre_del_animal
        self.sonido = sonido_que_hace

    def saludo(self):
        print('Esta mascota es un', self.tipo, 'se llama', self.nombre, 'y hace', self.sonido)

class Gato(Animal):
    tipo = 'gato'

class Perro(Animal):
    tipo = 'perro'

gato_uno = Gato(nombre_del_animal='Manchas', sonido_que_hace='Miau!')
gato_uno.saludo()

perro_uno = Perro('Kima', 'Guau!')
perro_uno.saludo()
