# Sergio Garino Vargas 
# Fecha: 12/1/2023
# Ejercicios para practicar lo aprendido hasta ahora
# Escribir un programa que devuelva el volumen de una esfera con base en el 
# radio

def calcular_vol(radio):
    vol = 4/3 * 3.1415 * (radio**3) # Formula de volumen de una esfera
    return vol

esfera_uno = calcular_vol(5)
print(esfera_uno)