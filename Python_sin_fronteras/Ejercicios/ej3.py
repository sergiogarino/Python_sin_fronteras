# Sergio Garino Vargas 
# Fecha: 12/1/2023
# Ejercicios para practicar lo aprendido hasta ahora

# Escribir una función que encuentre el núemro menor de una lista

list = [1, 50, 100, 55, 7000, 3, 22, 1998, 8]

def num_menor():
    # Initialize a variable to keep track of the smallest number
    menor = 'init'

    # Iterate through each element in the list
    for x in list:
        if menor == 'init':
            menor = x
        else:
            menor = x if x < menor else menor

    print(menor)
    

num_menor()