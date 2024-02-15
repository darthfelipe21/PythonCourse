def suma():
    n1 = int(input("ingrese primer numero: "))
    n2 = int(input("ingrese segundo numero: "))
    print(n1 + n2)
    print("Listo!!!")

try:
    # Codigo a probar
    suma()
except TypeError:
    # Codigo a ejecutar si hay un error
    print("no puedes cocatenar un str con un int")

except ValueError:
    # Codigo a ejecutar si hay un error
    print("solo puedes ingresar numeros, no letras, ni caracteres especiales")
else:
    # Codigo a ejecutar si no hay error
    print("No hay problema")
finally:
    # Codigo que se va a ejcutar de todos modos
    print('Hasta aqui llegamos')