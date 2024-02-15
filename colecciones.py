from collections import Counter, defaultdict, namedtuple, deque

# Counter: Contar elementos
numeros = [8, 6, 7, 9, 8, 6, 7, 10, 11, 12, 12, 10, 8, 9, 6]

print(Counter(numeros))   # El resultado es una subclase de diccionario

print(Counter("Venezuela"))
print(Counter("al pan pan al vino vino".split()))

print("\n")

serie = Counter([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3])
print(serie.most_common())
print(serie.items())

print(serie.total())


# Defaultdict, una de sus ventjas que es que al iterar sobre un diccionario, si no conisgue un elemento no dara error
mi_dic = {'uno': 'verde', 'dos': 'azul', 'tres': 'morado', 'cuatro': 'amarillo'}
#print(mi_dic['cinco'])  # Esto daria un error

otro_dic = defaultdict(lambda: 'nada')
otro_dic['uno'] = 'violeta'
print(otro_dic['dos'])  # Asigna el valor por defecto declarado en el lambda
print(otro_dic)   # Ademas de no exisitir crea el nuevo key con el valor por default

# Namedtuple, son tuplas predefinidas, algo como la programación orientada a objetos
Persona = namedtuple('Persona', ['nombre', 'apellido', 'edad'])
cliente = Persona('Felipe', 'Martinez', 38)
print(cliente.edad)
print(cliente[1])

# Deque is preferred over a list in the cases where we need quicker append and pop operations

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

lista_ciudades.pop()

lista_ciudades.appendleft('Caracas')

lista_ciudades.insert(2, 'Santiago')

print(lista_ciudades)