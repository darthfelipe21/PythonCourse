import shutil
import zipfile

# Crear un archivo comprimido
archivo = zipfile.ZipFile('archivo_comprimido.zip', 'w')

with open('prueba1.txt', 'w') as file1:
    file1.write('Hola')

with open('prueba2.txt', 'w') as file2:
    file2.write('Chao')

archivo.write('prueba1.txt')
archivo.write('prueba2.txt')

archivo.close()

# Descomprimir archivo
archivo_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')

archivo_abierto.extractall()

archivo_abierto.close()


# Lo mismo usando shutil

carpeta_origen = '/Users/felipemartinez/Desktop/pythonProject/Day 9/practica_shutil'

archivo_destino = 'comprimido_shutil'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

# Descomprimir en shutil

shutil.unpack_archive('comprimido_shutil.zip', 'extraccion_shutil', 'zip')