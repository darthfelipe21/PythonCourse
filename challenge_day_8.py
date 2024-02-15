from generadores_decoradores_challege_day_8 import contadores, decorar_ticket
import time
def seleccion():
    letra = 'x'

    while letra not in 'cfp':
        print("Bienvenido a la Farmacia Pro")
        print("Seleccione categoria para ser atendido:")
        letra = input("""
        (C) Cosmeticos
        (F) Farmacia
        (P) Perfumeria
        """).lower()

    return letra


x = seleccion()
y = {'p': contadores(x), 'c': contadores(x), 'f': contadores(x)}

arranque = decorar_ticket(lambda: print(f"{x.upper()} - {next(y[x])}"))

while True:
    arranque()
    time.sleep(2)
    x = seleccion()





