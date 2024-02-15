class Configuracion:
    configuraciones_globales = {}

    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
        Configuracion.configuraciones_globales[nombre] = valor

    @classmethod
    def obtener_configuraciones(cls):
        return cls.configuraciones_globales

conf1 = Configuracion('MAX_RESULTADOS', 100)
conf2 = Configuracion('TIEMPO_ESPERA', 30)

configuraciones = Configuracion.obtener_configuraciones()

print(configuraciones)