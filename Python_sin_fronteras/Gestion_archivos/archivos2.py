# Sergio Garino Vargas 
# Fecha: 12/1/2023
# Progrmación para manipular archivos

import os

file = open('chanchito2.txt', 'a')

# Para escribir en un archivo se usa el método de .write()
file.write('\nNueva linea en mi archivo')

file.close()

os.remove('chanchito2.txt')

if os.path.exists('chanchito2.txt'):
    os.remove('chanchito2.txt')
else:
    print('File not found')
