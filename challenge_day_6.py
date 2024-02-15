from pathlib import Path
import os


base = Path.home()
ruta = Path(base, 'Desktop', 'Recetas')
print('Bienvenido al recetario')
print(f'Actualmente las recetas se encuentran en la siguiente ruta: {ruta}')


def categorie():
    folders = {}
    for enu, txt in enumerate(Path(ruta).glob('*/'), 1):
        folders[enu] = txt.stem
    return folders


def bienvenida():
    contador = 0
    for i in ruta.iterdir():
        if i.is_dir():
            contador += 1
    print(f'Existen {contador} recetas dentro del directorio')


def opciones():
    opcion = input(' 1- Leer receta\n 2- Crear receta\n 3- Crear categoria\n'
          ' 4- Eliminar receta\n 5- Eliminar categoria\n 6- Finalizar programa\n Eliga que operación quiere realizar: ')
    if opcion.isalpha():
        print('Elegir una de las siguientes opciones, solo por numeros:'
              '\n 1- Leer receta\n 2- Crear receta\n 3- Crear categoria\n'
          ' 4- Eliminar receta\n 5- Eliminar categoria\n 6- Finalizar programa')

    return int(opcion)


def categoria_nombre(cat):
    categorias = categorie()
    choice = ''
    for i, j in categorias.items():
        if cat == i:
            choice = j
    return choice


def categoria():
    categorias = categorie()
    opcion = [f"{clave}: {valor}" for clave, valor in categorias.items()]
    eleccion = 0
    print('\n'.join(opcion))
    cat = int(input('Seleccione una categoria (por número) o presione 0 para regresar: '))
    if cat == 0:
        return eleccion
    else:
        if cat not in categorias.keys():
            print('Categoria con ese número no existe')
            categoria()
        else:
            eleccion = categoria_nombre(cat)
    return eleccion


def receta_elegida():
    carpeta = categoria()
    archivos = {}
    if carpeta == 0:
        print("Volviendo al menú principal.")
        return None, None, None

    elif len(os.listdir(Path(ruta, carpeta))) > 0:
        for enumerar, txt in enumerate(Path(ruta, carpeta).glob('*.txt'), 1):
            archivos[enumerar] = txt
            print(f'{enumerar}: {txt.stem}')
        elegir_receta = int(input('Elegir una de las recetas mencionadas: '))
    else:
        print('No existen recetas en esta categoria o esa receta no existe')
        receta()
        return None, None, None
    return carpeta, archivos, elegir_receta


def receta():
    eleccion = ''
    carpeta, archivos, elegir_receta = receta_elegida()
    if carpeta is None:
        return
    for i, j in archivos.items():
        if elegir_receta == i:
            eleccion = j
    lectura = Path(ruta, carpeta, eleccion)
    if elegir_receta in archivos.keys():
        with open(lectura, 'r') as file:
            print('*' * 20, '\n')
            print(file.read(),'\n')
            print('*'*20, '\n')
    elegir_opcion()


def opcion_dos():
    pick_cat = categoria()
    if pick_cat == 0:
        return
    ruta2 = Path(base, 'Desktop', 'Recetas')
    os.chdir(Path(ruta2, pick_cat))
    nueva_receta = input('Ingresar nombre de la nueva receta: ')
    descripcion_receta = input(f'Escriba receta para {nueva_receta}: ')
    with open(nueva_receta + '.txt', 'w') as file:
        file.write(descripcion_receta)
    return


def opcion_tres():
    categorias = categorie()
    nueva_categoria = input('Ingresar nombre de la nueva categoria: ')
    os.mkdir(Path(base, 'Desktop', 'Recetas', nueva_categoria))
    categorias[5] = nueva_categoria
    elegir_opcion()


def opcion_cuatro():
    archivos = {}
    carpeta = categoria()

    if carpeta == 0:
        return

    eleccion = '' + '.txt'

    if len(os.listdir(Path(ruta, carpeta))) == 0:
        print(f"No hay recetas en esta categoria.")
        return

    else:
        for enumerar, txt in enumerate(Path(ruta, carpeta).glob('*.txt'), 1):
            archivos[enumerar] = txt
            print(f'{enumerar}: {txt.stem}')
        elegir_receta = int(input('Elegir receta ha eliminar: '))
        for i, j in archivos.items():
            if elegir_receta == i:
                eleccion = j

    if os.path.exists(eleccion):
        os.remove(eleccion)
        print(f"El archivo '{eleccion}' ha sido borrado.")
    else:
        print(f"El archivo no existe.")
        return
    return


def opcion_cinco():
    carpeta = categoria()

    if carpeta == 0:
        return

    eliminar = Path(ruta, carpeta)
    if os.path.exists(eliminar):
        os.rmdir(eliminar)
        print(f'La carpeta "{eliminar}" ha sido eliminada')
    else:
        print('La carpeta no existe')
        return
    return


def elegir_opcion():
    num = 0
    while num != 6:
        num = opciones()
        os.system('clear')
        if num == 1:
            receta()
        elif num == 2:
            opcion_dos()
        elif num == 3:
            opcion_tres()
        elif num == 4:
            opcion_cuatro()
        elif num == 5:
            opcion_cinco()
        elif num == 6:
            print('Gracias por venir!!!')
            break
        else:
            print('Ingrese solo valores indicados por el sistema')


elegir_opcion()






