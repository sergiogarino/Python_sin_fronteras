# Sergio Garino Vargas 
# Fecha: 2/1/2023
# Aplicación: Calculadora que suma 2 números 

dato1 = input('Ingrese el primer sumando: ')
dato2 = input('INgrese el segundo sumando: ')

# Lo siguiente causará un error pues concatenará los datos ingresados en vez de sumarlos 
# debido a que al usar 'input()' el dato ingresado se interpreta como un string

print(dato1 + dato2)

# Por lo tanto hay que hacer la conversión a tipo de dato entero con 'int()'

sumando1 = int(dato1)
sumando2 = int(dato2)

print(sumando1 + sumando2)
