import time

def prueba_uno(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_dos(numero2):
    lista = []
    contador = 1
    while contador <= numero2:
        lista.append(contador)
        contador += 1
    return lista


inicio = time.time()
prueba_uno(100000)
final = time.time()
print(final - inicio)

inicio2 = time.time()
prueba_dos(100000)
final2 = time.time()
print(final2 - inicio2)


import timeit

declaracion = """
prueba_uno(10)
"""

mi_setup = """
def prueba_uno(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
"""

duracion = timeit.timeit(declaracion, mi_setup, number = 1000000)   # Number es el numero de veces que se repite el codigo

print(duracion)