import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return self.formula_calculo_area(self.radio)

    @staticmethod
    def formula_calculo_area(radio):
        return math.pi * radio ** 2

# Uso de la clase
radio_circulo = 5
circulo = Circulo(radio_circulo)
area = circulo.calcular_area()
print(f"El área del círculo con radio {radio_circulo} es: {area}")





class Persona:
    _instancias = []

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        Persona._instancias.append(self)

    @classmethod
    def obtener_instancias(cls):
        return cls._instancias

# Crear algunas instancias
persona1 = Persona("John", "Doe")
persona2 = Persona("Jane", "Doe")

# Acceder a todas las instancias a través del método 'obtener_instancias'
todas_las_personas = Persona.obtener_instancias()
for persona in todas_las_personas:
    print(f"{persona.nombre} {persona.apellido}")