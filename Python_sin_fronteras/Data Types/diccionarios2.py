# Creamos un diccionario de dicionarios, estos se llaman 'diccionarios anidados'
gatitos = {
  "Fluffy": {
    "nombre": "Fluffy",
    "edad": 4,
  },
  "Mamba": {
    "nombre": "Black Mamba",
    "edad": 12
  }
}
# Imprimimos el diccionario
print(gatitos)

# Otra forma de crear diccionarios anidados es haciendolo por separado
gato1 = {
  "nombre": "negro",
  "edad": 1
}

gato2 = {
  "nombre": "macho claro",
  "edad": 2
}

gato3 = {
  "nombre": "machito",
  "edad": 3,
}

gato4 = {
  "nombre": "gris",
  "edad": 4
}

# Este es el diccionario anidado
gatitos2 = {
  "gato1": gato1,
  "gato2": gato2,
  "gato3": gato3,
  "gato4": gato4
}

# Imprimir el diccionario anidado
print(gatitos2)

# El constructor dict nos permite crear diccionarios, el primer paso es crear una variable en la 
# cual se llama la funcion dict() y se asignan los valores

perritos = dict(nombre = "Doggy", edad = 13)
print(perritos)

gatitos3 = dict(g1 = gato1, g2 = gato2)
print(gatitos3)


