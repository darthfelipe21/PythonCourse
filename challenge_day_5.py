from random import *

palabras= ['chelsea', 'manchestercity', 'everton', 'astonvilla', 'liverpool']
letras_correctas= []
letras_incorrectas= []
intentos= 6
aciertos= 0
juego_terminado= False

print('Bienvenido al juego del ahorcado, la palabra es un equipo de la Premier League y tienes 6 intentos para adivinarla')


def elegir_palbra(word_list):
    palabra_elegida= choice(word_list)
    letras_unicas= len(set(palabra_elegida))

    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida= ''
    es_valida= False
    abc= 'abcdefghijklmnopqrstuvwxyz'
    while not es_valida:
        letra_elegida= input('Ingrese una letra: ').lower()
        if letra_elegida in abc and len(letra_elegida) == 1:
            es_valida= True
        else:
            print('Información ingresada erronea')
    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta= []

    for i in palabra_elegida:
        if i in letras_correctas:
            lista_oculta.append(i)
        else:
            lista_oculta.append('_')

    print(' '.join(lista_oculta))


def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print('Ya adivinaste esta letra')

    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1


    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias


def perder():
    print('Se acabaron las vidas')
    print('La palabra era ' + palabra)

    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print('Felicitaciones!!!')
    return True

palabra, letras_unicas= elegir_palbra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: '+ '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra= pedir_letra()

    intentos, terminado, aciertos= chequear_letra(letra, palabra, intentos, aciertos)

    juego_terminado = terminado
