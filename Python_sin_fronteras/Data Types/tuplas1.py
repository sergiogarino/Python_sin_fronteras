# Creamos nuestra primera tupla
tupla1 = ('hola', 'esto', 'es', 'una', 'tupla', 'de', 'strings', 'hola')
print(tupla1)

# Guardamos el resultado de .count() en una variable x
x = tupla1.count('hola')

# Guardamos el resultado de .index en una variable y
y = tupla1.index('strings')

# Imprimimos el resultado
print(x, y)


# Para convertir una tupla en una lista se usa la función 'list()'
listaDeTupla = list(tupla1)
print(listaDeTupla)

