
sellers = ['felipe', 'indhira', 'leia']
name = input("Ingrese el nombre de vendedor: ").lower()
item = input("Ingrese venta del día: ")

def commission(name, item):
    if name not in sellers:
        print("Vendedor no registrado")
    elif not item.isdigit():
        print('Ingresar solo números')
    else:
        name= name.capitalize()
        item = round(float(item) * 0.13, 2)
        print(f"El vendedor {name} obtuvo una comisión de {item}")

commission(name, item)
