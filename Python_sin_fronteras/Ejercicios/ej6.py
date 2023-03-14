# Sergio Garino Vargas 
# Fecha: 12/1/2023
# Ejercicios para practicar lo aprendido hasta ahora
# Escribir una función que indique si un número es par o impar

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def paridad(list):
    for num in list:
        if num % 2 == 0:
            print(num, 'es un número par')
        else:
            print(num, 'no es un número par')

paridad(list)
