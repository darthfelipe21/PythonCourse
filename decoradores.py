# Decoradores
def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())


# Se puede asignar a una variable una funcion, no precisamente por el return
funcion_prueba = mayusculas
funcion_prueba("prueba")


# Igual se puede pasar una funcion a otra funcion
def otra_funcion(funcion):
    return funcion

otra_funcion(minusculas("OTRA PRUEBA"))

# Todo en uno
def cambiar_letra_dec(tipo):

    def mayus_deco(texto):
        print(texto.upper())

    def minus_deco(texto):
        print(texto.lower())

    if tipo == 'M':
        return mayus_deco
    elif tipo == 'm':
        return minus_deco


variable = cambiar_letra_dec('M')

variable('probadera')


# Ahora si decorar
def decorar_saludo(funcion):

    def otra_funcion_dec(palabra):
        print("hola")
        funcion(palabra)
        print('adios')
    return otra_funcion_dec


otra_variable = decorar_saludo(mayusculas)

otra_variable("texto decorado")


def prueba():
    def prueba2():
        print("hola que hace")
    return prueba2()

prueba()