# Sergio Garino Vargas 
# Fecha: 6/1/2023
# Orientación a objetos, descubriendo el concepto de herencia

# Creo una clase
class User:
    def __init__(self, name, last_name):

        self.name = name
        self.last_name = last_name

    def greeting(self):
        print('Hi, my name is', self.name, self.last_name)

# Creando una clase utilizando herencia
class Admin(User):
    def super_greeting(self):
        print('Hello, my name is', self.name, self.last_name, 
                ', and I am the Administrator of this page')

# Instancio un objeto de la clase User
user_1 = User('Marcos', 'Ramirez')

# Instancio un objeto de la clase heredada
super_user = Admin('Aida', 'Chacón')

# Utilizo métodos
user_1.greeting()
super_user.super_greeting()

# Output
# Hi, my name is Marcos Ramirez
# Hello, my name is Aida Chacón , and I am the Administrator of this page

