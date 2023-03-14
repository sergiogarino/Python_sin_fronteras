# Sergio Garino Vargas 
# Fecha: 3/1/2023
# Aplicación: Calculadora que suma 2 números y verifica la entrada

dato1 = input('Ingrese el primer sumando: ')

# Verificamos intentando hacer la conversión a entero, si no se puede, se asigna al sumando n
# es un string genérico                        
try:
    sumando1 = int(dato1)
except:
    sumando1 = 'El primer sumando ingresado no es un número'

dato2 = input('Ingrese el segundo sumando: ')

try:
    sumando2 = int(dato2)
except:
    sumando2 = 'El segundo sumando ingresado no es un número'

if (sumando1 == 'El primer sumando ingresado no es un número' or
    sumando2 == 'El segundo sumando ingresado no es un número'):
    print('Datos mal ingresados, intenta de nuevo')
else:                          
    print(sumando1 + sumando2)
