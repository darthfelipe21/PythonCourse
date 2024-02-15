import random


class Persona:
    instancias = []

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        Persona.instancias.append(self)

    @classmethod
    def obtener_instancias(cls):
        return cls.instancias


class Cliente(Persona):

    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.balance = 0
        self.num_cuenta = self.crear_cuenta()

    def mostrar(self):
        print(f'''
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Cuenta: {self.num_cuenta}
        Balance: {self.balance}''')

    def depositar(self):
        deposito = int(input("Ingrese la cantidad que desea depositar: "))
        self.balance += deposito
        print(f"Deposito exitoso, ahora su saldo es de: ${self.balance}")

    def retirar(self):
        retiro = int(input("Ingrese la cantidad que desea retirar: "))

        if self.balance < retiro:
            print("Saldo insuficiente")
            self.retirar()

        else:
            self.balance -= retiro
            print(f"Su saldo ahora es de: ${self.balance}")

    @staticmethod
    def crear_cuenta():
        num_cuenta = random.randint(10**9, (10**10)-1)
        return num_cuenta


def crear_usuario():
    nombre_cliente = input("Ingrese su nombre: ")
    apellido_cliente = input("Ingrese su apellido: ")
    cliente = Cliente(nombre_cliente, apellido_cliente)
    cliente.mostrar()
    return cliente


def quiero_depositar(cliente):
    cliente.depositar()


def quiero_retirar(cliente):
    cliente.retirar()


def elegir():
    eleccion = 0
    while eleccion not in range(1, 5):
        print("Elegir una de las siguientes opciones: ")
        eleccion = int(input("""
        (1) - Deposito
        (2) - Retirar
        (3) - Balance
        (4) - Salir del sistema
        Ingresar: """))

    return eleccion


def inicio(cliente):
    numero = elegir()
    if numero == 1:
        quiero_depositar(cliente)
        inicio(cliente)
    elif numero == 2:
        quiero_retirar(cliente)
        inicio(cliente)
    elif numero == 3:
        print(f"Su saldo es de: {cliente.balance}")
        inicio(cliente)
    else:
        print("Hasta pronto")


cliente1 = crear_usuario()
inicio(cliente1)
