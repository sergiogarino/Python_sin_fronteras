# def myFunction():
#     print('Hola, esta en una función en python')

# def printData(argument1):
#     print('Mi argumento es', argument1)

# printData(5)
# printData('Sergio')
# printData()
# printData('g', 5)

# def functArgsVariables(*nombre):
#     print('Nombre completo: ', nombre)

# functArgsVariables('Sergio', 'Garino', 'Vargas')

# def nombre_completo(nombre, apellido):
#     print(nombre, apellido)

# nombre_completo('Andrea', 'Cruz')
# nombre_completo(nombre='Sergio', apellido='Garino')


# def nombre_completo_2(**sergio):
#     print(sergio['nombre'], sergio['apellido'])

# nombre_completo_2(nombre='Sergio', apellido='Garino')

# def nombre_3(**kwargs):
#     print(kwargs['nombre'], kwargs['apellido'])
# nombre_3(nombre='Andrea', apellido='Cruz')

# def concatenaNombres(lista):
#     i = '' 
#     for el in lista:
#         i = i + el + ' '
#     return i

# nombres = concatenaNombres(['sergio', 'alberto', 'garino', 'vargas'])
# print(nombres)

def recursion(i):
    if (i < 1):
        return i
    print(i)
    recursion(i-1)

recursion(5)


