# Manera que se puede usar si para evitar errores de input
def pedir_numero():
    while True:
        try:
            numero = int(input("ingrese un numero: "))
        except:
            print("no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("gracias")


def cociente(num1, num2):
    try:
        x= num1 / num2
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
    else:
        print(x)


cociente('dos', 10)