# Generador de conteo
def contadores(x):
    p = 0
    c = 0
    f = 0
    while True:
        if x == 'p':
            p += 1
            yield p
            if p == 99:
                p = 0
        elif x == 'f':
            f += 1
            yield f
            if f == 99:
                f = 0
        elif x == 'c':
            c += 1
            yield c
            if c == 99:
                c = 0

# Decorador de tickets
def decorar_ticket(funcion):

    def ticket():
        print('\n')
        print('*' * 20)
        print("Su turno es:")
        funcion()
        print("aguarde y sera atendido")
        print('*' * 20)
        print('\n')
    return ticket







