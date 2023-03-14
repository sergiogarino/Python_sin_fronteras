# Creamos una lista con varios elementos repetidos
lista = [1, 2, 3, 3, 3, 4, 5]

# Con el uso de .count podemos ver que el elemento '3' se repite tres veces
print(lista.count(3))
print(lista.count(50))

# Con la función len() se puede contar la cantidad de elementos en lista
cantidad_elementos = len(lista)
print(cantidad_elementos)

print(lista)

lista.append(22)
print(len(lista))

print(lista)


