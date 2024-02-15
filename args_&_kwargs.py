# *args nos permite cargar o pasas un cantidad n de argumentos iterables a una función
def suma(*args):
    total= 0
    for a in args:
        total += a
    return total

print(suma(1, 2, 3, 50, 100, 550, 6))


# Suma de numeros elevados al cuadrado
def suma_cuadrados(*args):
    suma = 0
    for i in args:
        suma += i ** 2
    return suma


print(suma_cuadrados(1, 2, 3))


# Suma de numeros absolutos
def suma_absolutos(*args):
    total= 0
    for i in args:
        total += abs(i)
    return total

print(suma_absolutos(-1, -50, 50, -100))

# Strings y numeros como argumentos
def numeros_persona(*args):
    n= ''
    suma_numeros= 0
    for i in args:
        if type(i) == str:
            n= i.capitalize()
        else:
            suma_numeros += i
    print(f'{n}, la suma de tus números es {suma_numeros}')

numeros_persona('felipe', 1, 2, 5, 7, 21)


def numeros_persona2(n, *args):
    suma_numeros= 0
    for i in args:
        suma_numeros += i
    return(f'{n.capitalize()}, la suma de tus números es {suma_numeros}')

print(numeros_persona2('felipe', 1, 2, 5, 7, 21))


# (**kwargs)Key words arguments
def diccionario(**kwargs):
    print(type(kwargs))
    total= 0
    for clave, valor in kwargs.items():
        print(clave, '= ', valor)
        total += valor
    return(total)

print(diccionario(a= 2, b= 5, c= 100))


# Función todo en uno
def all_in_one(x, y, *args, **kwargs):  # Este deberia de ser el orden si se usara todo
    print(f'Primer argumento= {x}')
    print(f'Segundo argumento= {y}')
    for e, i in enumerate(args, 1):
        print(f'Args #{e} = {i}')
    print(f'Kwargs')
    for c, v in kwargs.items():
        print(f'{c} = {v}')

all_in_one('hola', 5, 21, 10, 1985, 'Que paso', m= 'mamá', p= 'papá', h= 'hijo', f= 3)

args= [1, 2, 3, 4, 5]
kwargs= {'a': 'avión', 'l': 'lado', 'r': 'ratón'}
all_in_one('primero', 'segundo', *args, **kwargs)


# Contar cantidad de atributos en kwargs
def cantidad_atributos(**kwargs):
    total= 0
    for c, v in kwargs.items():
        total += 1
    return total

print(cantidad_atributos(m= 'mamá', p= 'papá', h= 'hijo', f= 3))


# Traer solo los valores de los elementos pasados por kwargs en una lista
def lista_atributos(**kwargs):
    lista= []
    for c,v in kwargs.items():
        lista.append(v)
    return lista

print(lista_atributos(m= 'mamá', p= 'papá', h= 'hijo', f= 3))


# Descripción de una persona con key words arguments

def describir_persona(n, **kwargs):
    print(f'Características de {n}:')
    for c,v in kwargs.items():
        print(f'{c}: {v}')

describir_persona("María", color_ojos="azules", color_pelo="rubio")