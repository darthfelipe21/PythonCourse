from os import system

# Archivo guardado en la carpeta de este mismo codigo

with open("Prueba.txt", "r", encoding="latin-1") as archivo:
    print(archivo.read())
    print(archivo.readline())


with open("Prueba.txt", "r", encoding="latin-1") as archivo:
    print(archivo.readline())


with open("Prueba.txt", "r", encoding="latin-1") as archivo:
    for i in archivo:
        print('Esta linea dice: ' + i)

with open("Prueba.txt", "r", encoding="latin-1") as archivos:
    lista= archivos.readlines()
    print(lista)

'''Con "with open" no es necesario cerrar el archivo'''


# Crear o escribir un archivo

with open('nuevo_archivo.txt', 'w') as file:
    file.write('Texto en nuevo archivo')


# Agregar contenido a un archivo sin perder lo que ya tiene

with open('nuevo_archivo.txt', 'a') as file:
    file.write('\nSegunda linea de texto, en el archivo')

"""Si se usa la w en un archivo existente, borrara todo su contenido e ingresara lo que que se haya indicado"""
# Agregar varias lineas

with open('nuevo_archivo.txt', 'w') as file:
    file.write('''Estos son varias
    lineas de texto
    en el archivo''')

# Cocatenar varios elementos de una lista en un archivo

with open('nuevo_archivo2.txt', 'w') as file:
    file.writelines(['hola', 'como', 'estas'])


# Crear archivo con iteración sobre una lista

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

with open('registro.txt', 'w') as file:
    for i in registro_ultima_sesion:
        file.writelines(i + '\t')

with open('registro.txt', 'r') as file:
    print(file.read())

system('clear')

archivo= 'registro.txt'
def abrir_leer(archivo):
    with open(archivo, 'r') as file:
        print(file.read())


abrir_leer(archivo)