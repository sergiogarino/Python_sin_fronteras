# Sergio Garino Vargas 
# Fecha: 12/1/2023
# Ejercicios para practicar lo aprendido hasta ahora
# Escribir una función que determine si un usuario es mayor de edad utilizando
# clases

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age 


def mayor_de_edad(user):
    return user.age >= 18

user_1 = User('Kono Cruz Retana', 19)
user_2 = User('Kima Cruz Retana', 15)

result_1 = mayor_de_edad(user_1)
result_2 = mayor_de_edad(user_2)

print(result_1)
print(result_2)