import os

# Verificar el  directorio actual
ruta = os.getcwd()
print(ruta)

# Cambiar directorio
ruta= os.chdir('/Users/felipemartinez/Desktop')
revisar= os.getcwd()
print(revisar)

# Crear una carpeta desde python
os.mkdir('/Users/felipemartinez/Desktop/prueba')

# Borrar un carpeta
os.rmdir('/Users/felipemartinez/Desktop/prueba')

# Crear un ruta base y poder manipularla sin reescribirlo

camino= '/Users/felipemartinez/Desktop/pythonProject/Day 6/prueba.txt'
element= os.path.dirname(camino)  # Direcctorio
elemento= os.path.basename(camino)  # Archivo
element_in_tuple= os.path.split(camino)
print(element,'\n',elemento, '\n', element_in_tuple)


from pathlib import Path

principal= Path('/Users/felipemartinez/Desktop/pythonProject/Day 6/')
archivo= principal / 'prueba.txt'

with open(archivo, 'r', encoding="latin-1") as files:
    print(files.read())


# Sin usar el open se puede ejecutar el path

variable= Path('/Users/felipemartinez/Desktop/pythonProject/Day 6/nuevo_archivo.txt')
print('________________________________________')
print(variable.read_text())
print(variable.name)
print(variable.stem)
print(variable.suffix)

if not variable.exists():
    print('No existe')
else:
    print('Existe')

# Accesos a tarves de path

base= Path.home()
print(base)

guia= Path(base, 'desktop', 'pythonproject', 'day 6')
guia2= guia.with_name("day_5")
print(guia)
print(guia2)

# Mostrar antecesor inmediato de una ruta

print(guia.parent)
print(guia.parent.parent)
print(guia.parents[2])

# Mostrar todos los archivos con un suffix especifico

for enu, txt in enumerate(Path(guia).glob('*.txt'), 1):
    print(f'{enu} = {txt.stem}')

# Mostrar todas las carpetas o sub carpetas dentro de una ruta

for todo in Path(guia).glob('**/*'):
    print(todo)
