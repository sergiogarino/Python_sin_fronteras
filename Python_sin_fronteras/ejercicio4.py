# Sergio Garino Vargas 
# Fecha: 3/1/2023
# Aplicación: Calculadora que suma 2 números y verifica la entrada al momento de que se ingresa

dato1 = input('Ingrese el primer sumando: ')

# Verificamos intentando hacer la conversión a entero, si no se puede, se asigna al sumando n
# es un string genérico                        
try:
    sumando1 = int(dato1)
except:
    sumando1 = 'El primer sumando ingresado no es un número'

if sumando1 == 'El primer sumando ingresado no es un número':
    print("El primer dato ingreasado no es un número entero")
    exit()


dato2 = input('Ingrese el segundo sumando: ')

try:
    sumando2 = int(dato2)
except:
    sumando2 = 'El segundo sumando ingresado no es un número'


if (sumando2 == 'El segundo sumando ingresado no es un número'):
    print('El segundo dato no es un entero, intenta de nuevo')
    exit()

print(sumando1 + sumando2)
