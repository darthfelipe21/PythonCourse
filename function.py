def todos_positivos(x):
    for i in x:
        if i < 0:
            return False
        else:
            pass
    return True

lista_numeros= [-1, 10, 50, -11]

print(todos_positivos(lista_numeros))



def suma_menores(x):
    suma= 0
    for i in x:
        if i > 0 and  i < 1000:
            suma += i
        else:
            pass
    return suma

lista_numeros= [1, 500, 10000, 50]

print(suma_menores(lista_numeros))




def cantidad_pares(x):
    pares= 0
    for i in x:
        if i%2 == 0:
            pares += 1
        else:
            pass
    return pares

lista_numeros= [1, 2, 3, 4, 5, 6, 7, 8]

print(cantidad_pares(lista_numeros))



# Verificar tupla mas cara dentro de una lista

precios_cafe= [('Capuccino', 1.5), ('Expresso', 2.5), ('Mokaccino', 2.0)]

def precio_mas_caro(c):
    caro= 0
    cafe= ''
    for x, y in c:
        if y > caro:
            caro= y
            cafe= x
        else:
            pass
    return (cafe, caro)  # Se pone entre parentesis para que devuelva una tupla

print(precio_mas_caro(precios_cafe))



# Palitos de la suerte
from random import shuffle

palitos= ['-', '--', '---', '----']

def mezclar(p):
    shuffle(p)
    return p

def choice():
    chosen= ''
    while chosen not in ['1', '2', '3', '4']:
        chosen= input('Elegir un numero entre el 1 y el 4: ')
    return int(chosen)

def selection(lista, choose):
    if lista[choose - 1] == '-':
        print('Perdiste!!!')
    else:
        print('Te salvaste')

    print(f'{lista[choose - 1]} no es el mas corto')

mixed= mezclar(palitos)
eleccion= choice()

selection(mixed, eleccion)


# Lanzamiento de dados
from random import *

def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return (dado1, dado2)


def evaluar_jugada(x, y):
    suma = x + y
    if suma <= 6:
        print(f'La suma de tus dados es {suma}. Lamentable')
    elif (suma > 6) and (suma < 10):
        print(f'La suma de tus dados es {suma}. Tienes buenas chances')
    else:
        print(f'La suma de tus dados es {suma}. Parece una jugada ganadora')

one, two= lanzar_dados()

evaluar_jugada(one, two)


# Eliminar duplicados de una lista
lista_numeros= [1, 2, 15, 7, 2]

def reducir_lista(lista):
    test= list(set(lista))
    test.pop()
    return test

def promedio(lista1):
    conteo= 0
    for i in lista1:
        conteo += 1
    return sum(lista1)/conteo

reducir= reducir_lista(lista_numeros)

chequeo= promedio(reducir)

print(chequeo)


# Lanzar moneda
lista_numeros = [10, 30, 55, 70, 2, 5]


def lanzar_moneda():
    return choice(['Cara', 'Cruz'])


def probar_suerte(moneda, numero):
    if moneda == 'Cara':
        numero.clear()
        print(f'La lista se autodestruira {numero}')
    else:
        print(f'La lista se ha salvado {numero}')


coin = lanzar_moneda()

probar_suerte(coin, lista_numeros)

