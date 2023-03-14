dato = input("Ingresar dato: ")

print(dato)

lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

# Recordemos que el método .count() devuelve la cantidad de veces que aparece un
# elemento en una lista, por lo tanto si aparece al menos una vez se puede interpretar
# que el elemento si existe
if lista.count(dato) > 0: 
    print ('El dato', dato, 'existe')
else:
    print('El dato', dato, 'no existe')