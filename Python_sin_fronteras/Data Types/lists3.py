# Creemos una lista de strings
lista = ['uno', 'dos', 'tres']

# Para acceder a los elementos usamos el nombre de la lista, paréntesis cuadrados y la posición 
# del elemento
print(lista)
print(lista[0],lista[1],lista[2])

# Creamos una nueva lista
lista2 = [1, 2, 3, 4, 5, 6, 7]
print(lista2)

# Eliminamos el último elemento de lista con .pop
lista2.pop()

# Imprimimos
print(lista2)

# Eliminamos el elemento 'dos' de lista con .remove
lista.remove('dos')

# Eliminamos el elemento '4' de lista2 con .remove
lista2.remove(4)

# Imprimimos
print(lista, lista2)

# Creamos una lista
lista4 = [1, 38, 2, 3, 77, 4, 15, 5, 60]
print("Esta es la lista:", lista4)

# Invertimos el orden con el método .reverse
lista4.reverse()
print("Esta es la lista invertida:", lista4)
 
# Ordenamos la lista de menor a mayor con .sort
lista4.sort()
print("Esta es la lista ordenada:", lista4)

