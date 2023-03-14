# Para crear un diccionario se utilizar llaves {}, sus elementos se dividen por comas y mediante 
# un string se define el elemento, luego se ponen dos puntos ':' y luego el valor de ese elemento.
# Por ejemplo un diccionario con carros
diccionario = {
  "marca": "Toyota",
  "modelo": "Yaris",
  "anio": 2011
}

# Imprimimos el diccionario
print(diccionario)

# Para acceder a cualquier elemento se usan paréntesis cuadrados [] o el método .get()
print(diccionario["marca"])
print(diccionario.get("modelo"))

# Para cambiar algún elemento en el diccionario 
diccionario["anio"] = 2022
print(diccionario)

# Para contar los elementos que hay en un diccionario se puede usar len()
print(len(diccionario))

# Para agregar un nuevo valor al diccionario
diccionario["funciona"] = 'SI'
print(diccionario)

# Para eliminar alguún elemento se puede utilizar el método .pop()
diccionario.pop("funciona")
print(diccionario)

# El método .popitem() elimina el último elemento que se ha agregado al diccionario
diccionario.popitem()
print(diccionario)

# El uso del la palabra reservada "del" permite eliminar elementos
del diccionario["modelo"]
print(diccionario)

# Se puede hacer una copia de un diccionario con el método de .copy() o la función dict
copiaDiccionario = diccionario.copy()
copiaDiccionario2 = dict(diccionario)
print(copiaDiccionario, copiaDiccionario2)

# Se pueden eleminar todos los elementos de un diccionario con el método .clear()
diccionario.clear()
print(diccionario)

