

#Ejercicio 9
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

palabra  = input ("ingresa palabra: ")

palabra = list(palabra)

con_a=0
con_e=0
con_i=0
con_u=0
con_o=0

for j in palabra:
    if j == "a":
        con_a=con_a +1
    elif j == "e":
        con_e=con_e +1
    elif j == "i":
        con_i = con_i +1
    elif j == "u":
        con_u = con_u +1
    elif j == "o":
        con_o = con_o +1

print (f'a:{con_a}, b: {con_e}, i: {con_i}, o: {con_o}, u: {con_u}')
