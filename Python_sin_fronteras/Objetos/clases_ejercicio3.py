# Sergio Garino Vargas 
# Fecha: 7/1/2023
# Extendiendo el método __init__ en clases heredadas


class Animal:
    def __init__(self, nombre_del_animal, sonido_que_hace):
        self.nombre = nombre_del_animal
        self.sonido = sonido_que_hace

    def saludo(self):
        print('Esta mascota es se llama', self.nombre, 'y hace', self.sonido)

class Perro(Animal):
    def __init__(self, nombre_del_animal, sonido_que_hace, raza, edad):
        Animal.__init__(self, nombre_del_animal, sonido_que_hace)        
        self.raza = raza
        self.edad = edad
        tipo = 'perro'
    
    def saludo(self):
        return super().saludo()

class Gato(Animal):
    def __init__(self, nombre_del_animal, sonido_que_hace, raza, edad, dueño):
        super().__init__(nombre_del_animal, sonido_que_hace)
        self.raza = raza
        self.edad = edad
        self.dueño = dueño

    def maullido(self):
        print('Soy un gato, mi raza es', self.raza, 'tengo', self.edad, 'meses y mi nombre es', self.nombre)


gato_uno = Gato(nombre_del_animal= 'Manchas', sonido_que_hace='Miau!', raza='Felino', edad=15, dueño='Sergio') 
gato_uno.saludo()
gato_uno.maullido()