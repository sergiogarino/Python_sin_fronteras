# Sergio Garino Vargas 
# Fecha: 12/1/2023
# Ejercicios para practicar lo aprendido hasta ahora
# Escribir una función que reciba n números hasta que se ingrese la palabra 
# 'end' y se calcule la suma de los números ingresados

list = []

print('Enter a number and press Enter, to stop enter "end"')

user_input = input('Number: ')
while user_input != 'end':
    try:
        user_input = int(user_input)
        list.append(user_input)
    except:
        print('Invalid input')
        exit()

resultado = 0

for num in list:
    resultado += num
print(resultado)
    