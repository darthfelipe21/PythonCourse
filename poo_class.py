class Carro:
    pass


mi_carro = Carro()
otro_carro = Carro()

# Chequear los print
print(mi_carro)    # Este estaria en una ubicación
print(otro_carro)   # Y este en otra ubicación

print(type(mi_carro))

print('\n', '*' * 50, '\n')

# Atributos de instancia y de clases
class Perro:
    animal = True    # Atributo de clase

    def __init__(self, name, raza, color):
        self.nombre = name   # Atributos de instancia
        self.raza = raza     # Atributos de instancia
        self.color = color   # Atributos de instancia


mi_perro = Perro('perrito', 'puddle', 'blanco')

print(mi_perro.nombre)  # Percatarme que el metodo del self de name esta con la definicion nombre
print(mi_perro.raza)
print(mi_perro.color)
print(mi_perro.animal)

print(Perro.animal)

print('\n', '*' * 50, '\n')
# Metodos para clases
class Peliculas:
    cine = True

    def __init__(self, nombre_pelicula, actor_principal, actor_reparto, genero):
        self.nombre_pelicula = nombre_pelicula
        self.actor_principal = actor_principal
        self.actor_reparto = actor_reparto
        self.genero = genero

    def mensaje(self):   # Metodo, init ya es un metodo
        print(f'Esta es una pelicula {self.genero}')

    def resena(self, resena):  # Otro metodo
        return f'Esta es la reseña de la pelicula: {resena}'


interstellar = Peliculas('Interstellar', 'Mathew McConnegi', 'Anne Hathaway', 'Ciencia - Ficción')

interstellar_resena = interstellar.resena('Super pelicula')

print(f'Información de la pelicula {interstellar.nombre_pelicula}, con los actores {interstellar.actor_principal} '
      f'y {interstellar.actor_reparto}, cuenta con la siguiente reseña {interstellar_resena}')

print('\n', '*' * 50, '\n')

# Decoradores

class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('Pio')

    # Metodos de instancia (acceder y modificar)
    def volar(self, metros):
        print(f'El pajaron volo {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    # Metodos de clase
    """Pueden ser ejecutados sin una instancia, si no existe instancia se podria llamar Pajaro.poner_huevos(3)
    y tampoco se puede acceder al contenido de otros metodos, mas si se pueden alterar los elementos de clases
    como en este caso alas"""
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False

    # Metodos estaticos
    """No aceptan como parámetro ni la instancia ni la clase. Es por ello por lo que no pueden modificar el estado 
    ni de la clase ni de la instancia. En otras palabras, los métodos estáticos se podrían ver como funciones normales, 
    con la salvedad de que van ligadas a una clase concreta."""
    @staticmethod
    def mirar():
        print("El pajaro mira")



piolin = Pajaro('amarillo', 'canario')

# Metodos de instancia (modificar estado de la clase)
piolin.alas = False

print(piolin.alas)

