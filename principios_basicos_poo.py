# 1 Herencia
class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)   # Traer todos los atributos heredados, sin necesidad de reesribir
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('Pio')
    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')

piolin = Pajaro(2, 'azul', 60)

mi_animal = Animal(5, 'rojo')

piolin.nacer()
piolin.hablar()
piolin.volar(100)

print(Pajaro.__bases__)
print(Animal.__subclasses__())

# Herencia multiple
class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('Ja,Ja')
    def hablar(self):
        print('Chao')
class Hijo(Padre, Madre):  # Se heredan las clases que estan declaradas primero, en este caso padre
    pass
class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
print(Nieto.__mro__)   # Orden de busqueda de ejecución


# 2 Polimorfismo
class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuuu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beeee")


vaca1 = Vaca('Cama')
oveja1 = Oveja('Lana')

animales = [vaca1, oveja1]

for animal in animales:
    animal.hablar()
"""El polimorfismo lo que nos muestra, es que independientemente de que existan metodos con el mismo nombre 
en cada clase el sistema no tendra confusiones en cuanto a los metodos de cada instancia"""

def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)
animal_habla(oveja1)



# 3 Cohesión

url = 'https://escueladirecta-blog.blogspot.com/2021/09/cohesion-pilares-de-la-programacion.html'

# 4 Abstracción

url2 = 'https://escueladirecta-blog.blogspot.com/2021/10/abstraccion-pilares-de-la-programacion.html'

# 5 Acoplamiento

url3 = 'https://escueladirecta-blog.blogspot.com/2021/10/acoplamiento-pilares-de-la-programacion.html'

# 6 Encapsulamiento

url4 = 'https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html'


palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

todos = [palabra, lista, tupla]

for i in todos:
    print(len(i))


class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


mago = Mago()
arquero = Arquero()
samurai = Samurai()

for i in arquero, mago, samurai:
    i.atacar()