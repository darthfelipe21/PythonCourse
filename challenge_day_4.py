from random import *

play = input('Te gustaria jugar? Y/N: ').lower()
def adivinar(play):
    while play == 'y':
        test = randint(1, 5)
        chance = 0
        player = input('Bienvenido al juego adivina el número \n Por favor ingresa tu nombre: ')
        x = int(input(
            f'Muy bien {player.capitalize()} ahora ingresa un número del 1 al 100 e intenta adivinar que estoy pensando, recuerda que tienes solo 8 intentos: '))
        while chance < 7:
            chance += 1
            if (x < 1) or (x > 100):
                print(f'El número {x} no esta dentro del rango de 1 y 100, te quedan {8-chance} intentos')
                x = int(input('Ingrese otro numero entre el 1 y 100: '))
            elif x < test:
                print(f'Ha elegido un número menor al número secreto, intente de nuevo, le quedan {8-chance} oportunidades')
                x = int(input('Ingrese otro numero entre el 1 y 100: '))
            elif x > test:
                print(f'Ha elegido un número mayor al número secreto, intente de nuevo, le quedan {8-chance} oportunidades')
                x = int(input('Ingrese otro numero entre el 1 y 100: '))
            if chance == 7:
                print(f'PERDISTE!!! El numero secretro era {test}')
                play = input('Te gustaria jugar de nuevo? Y/N: ').lower()
                break
            if x == test:
                print(f'FELICIDADES!!!\nAcertaste el número secreto y lo lograste en {chance} intento/s')
                play = input('Te gustaria jugar de nuevo? Y/N: ').lower()
                break
    print('Gracias por jugar')



adivinar(play)