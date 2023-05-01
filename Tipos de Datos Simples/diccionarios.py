
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia.
#  Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def contar_palabras ( frase ):
    lista = {}
    contador=0
    palabra = frase.split()
    print (palabra)
    for i in palabra:
        if i in lista:
            contador = contador +1
            lista[i] = contador
        else:
            lista[i] = 1
    return lista

def most_repeated(words):
    max_palabra = ''
    n_palabra = 0
    for word, freq in words.items():
        if freq > n_palabra:
            max_palabra = word
            n_palabra = freq
    return max_palabra, n_palabra

frase = input ('mete una frase: ')

print(contar_palabras(frase))
print(most_repeated(contar_palabras(frase)))
