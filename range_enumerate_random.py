# Crear una lista desde el 2500 al 2585
mi_lista = list(range(2500,2586))
print(mi_lista)

# Crear una lista de multiplos de 3 hasta el 300
mi_lista = list(range(3,301,3))
print(mi_lista)

# Sumar los cuadrados de todos los números del 1 al 15
suma_cuadrados = 0

for i in range(1,16):
    suma_cuadrados= suma_cuadrados + i**2

print(suma_cuadrados)


# Enumerate

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]


for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


lista_indices= list(enumerate("Python"))
print(lista_indices)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for i, o in enumerate(lista_nombres):
    if str(o).startswith('M'):
        print(i)



# Empaquetado o zip
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

packed= list(zip(capitales, paises))

for c, p in packed:
    print(f'La capital de {p} es {c}')




# Minimo y maximo
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima= min(diccionario_edades.values())

ultimo_nombre= max(list(diccionario_edades)).lower()

print(edad_minima, ultimo_nombre)



# RANDOM: randint (numero alematorio entre 2 numero enteros), choice (elige un elemento de una lista, dict, tuple), shuffle (desordena una ejecución), random (numero aleatorio entre 0 y 1), uniform (numero decimal entre 2 numeros)

from random import randint  # Tambien se pueden importar todos los metodos con un *

aleatorio= randint(1,10)

print(aleatorio)


from random import *
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

sorteo= choice(nombres)