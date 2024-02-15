# Los metodos especiales son aquellos que inician y terminan con __
mi_lista = [1, 1, 1, 1, 1, 1, 1]

class Objeto:
    pass

mi_objeto = Objeto()

print(mi_objeto)  # Esta ejecución trae un str informando que es de tipo objeto


class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se a eliminado la instancia")

mi_cd = CD('Pink Floyd', 'Te Wall', 24)

print(mi_cd)
"""Al declarar una funcion con __str__ taera el contenido de la instancia y no como objeto"""


del mi_cd  # Elimina una instancia
