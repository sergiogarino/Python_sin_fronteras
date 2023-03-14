# Sergio Garino Vargas 
# Fecha: 12/1/2023
# Ejercicios para practicar lo aprendido hasta ahora
# Contar las mayúsculas que hay en una palabra

word_1 = 'SergioAlbertoGarinoVargas'

def count_vocals(word):
    vowels = 0
    word_to_count = word.lower()
    print(word, word_to_count)
    for char in word:
        if (char == 'a' 
            or char == 'e' 
            or char == 'i' 
            or char == 'o' 
            or char == 'u'):
            
            vowels += 1
        else:
            vowels += 0
    
    print(vowels)

count_vocals(word_1)

            
