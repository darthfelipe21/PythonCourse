from os import system

nombre= input('Tu nombre: ')
apellido= input('Tu apellido: ')

system('clear')   # Para windowns es 'cls'

print(f'{nombre} {apellido}')

import os
from pathlib import Path
base = Path.home()
os.chdir(Path(base, 'Desktop', 'Recetas'))


rutas = os.getcwd()
print(rutas)