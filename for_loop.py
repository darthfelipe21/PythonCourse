alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for i in alumnos_clase:
    print('Hola ' + i, '\n')

lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_numeros = 0

for plus in lista_numeros:
    suma_numeros = suma_numeros + plus
    print(suma_numeros)

print('\n')
print(suma_numeros,'\n')



lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for a in lista_numeros:
    if a%2 == 0:
        suma_pares= suma_pares + a
    else:
        suma_impares= suma_impares + a

print(suma_pares, suma_impares)