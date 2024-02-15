def generador():
    for i in range(1, 5):
        yield i**2


generar = generador()

print(next(generar))

print(next(generar))


def generador2():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x

variable2 = generador2()

print(next(variable2))
print(next(variable2))
print(next(variable2))



def vidas():
    x = 3
    while x >= 0:
        if x == 3:
            print(f"Te quedan {x} vidas")
            x -= 1
        elif x == 2:
            print(f"Te quedan {x} vidas")
            x -= 1
        elif x == 1:
            print(f"Te queda {x} vida")
            x -= 1
        elif x == 0:
            print('Game Over')
            break
        yield

perder_vida = vidas()

next(perder_vida)
next(perder_vida)
next(perder_vida)
next(perder_vida)
next(perder_vida)


def mensaje():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x


perder_vida = mensaje()