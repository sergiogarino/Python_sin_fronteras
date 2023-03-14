# Sergio Garino Vargas 
# Fecha: 3/1/2023
# Aplicación: Calculadora que ejecuta las 4 operaciones básicas y verifica la entrada al 
# momento de que se ingresa, además verifica de que la operación deseada sea válida, siendo 
# validas +, -, *, /.

dato1 = input('Ingrese el primer sumando: ')

# Verificamos intentando hacer la conversión a entero, si no se puede, se asigna al sumando n
# es un string genérico                        
try:
    primer_numero = int(dato1)
except:
    primer_numero = 'El primer sumando ingresado no es un número'

if primer_numero == 'El primer sumando ingresado no es un número':
    print("El primer dato ingreasado no es un número entero")
    exit()

dato2 = input('Ingrese el segundo sumando: ')

try:
    segundo_numero = int(dato2)
except:
    segundo_numero = 'El segundo sumando ingresado no es un número'

if (segundo_numero == 'El segundo sumando ingresado no es un número'):
    print('El segundo dato no es un entero, intenta de nuevo')
    exit()

operacion = input('Ingrese el símbolo de la operación que quiere ejecutar: ')

if operacion == '+':
    print(primer_numero + segundo_numero)
elif operacion == '-':
    print(primer_numero - segundo_numero)
elif operacion == '*':
    print(primer_numero * segundo_numero)
elif operacion == '/':
    print(primer_numero / segundo_numero)
else:
    print('Operación no válida')
