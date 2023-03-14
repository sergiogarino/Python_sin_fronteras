# Sergio Garino Vargas 
# Fecha: 12/1/2023
# Ejercicios para practicar lo aprendido hasta ahora

# Multiplixar dos números sin usar el signo de multiplicación *
# La lógica es sumar a veces el número b, o viceverse, para hacer el proceso
# más eficiente, se busca iterar el menor númeor de veces, por eso, se compara
# y se itera con base en el menor número.
a = 800
b = 10
resultado = 0

if a > b:
    for num in range(b):
        resultado += a
else:
    for num in range(a):
        resultado += b

print(resultado)