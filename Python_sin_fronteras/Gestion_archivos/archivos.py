# Sergio Garino Vargas 
# Fecha: 12/1/2023
# Progrmación para manipular archivos

# Para abrir un archivo se usa la función open()
open_file = open('chanchito.txt')

# Para leer todo el archivo se usa el método .read()
print(open_file.read())

# Los permisos con los que se puede abrir un archivo son:
# Leer --> read = 'r', lee un archivo existente
# Agregar --> append = 'a', agrega contenido al final de un archivo existente
# Sobreescribir o crear --> write = 'w', sobreescrive todo el contenido de un
# archivo existente, si el archivo no existe lo crea.
# Crear --> create = 'x', si el archivo no exiaste crea uno nuevo, si ya existe
# devuelve error.
# Cualquiera de esos permisos se le pasan como segundo parámetro a la función
# open()

open_file_read = open('chanchito.txt', 'r')
open_file_append = open('chanchito.txt', 'a')
open_file_write = open('chanchito2.txt', 'w')
#open_file_create = open('holamundo.txt', 'x')

open_file_read.close()
open_file_append.close()
open_file_write.close()
#open_file_create.close()

# Para leer un archivo linea por linea se utiliza el método de .readline()

file = open('chanchito.txt')
print(file.readline())
print(file.readline())


for line in file:
    print(line)

file.close()


