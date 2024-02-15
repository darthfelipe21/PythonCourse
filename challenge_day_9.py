import zipfile
import re
import os
from pathlib import Path
from datetime import datetime
import time
import math
"""# Descomprimir archivo en carpeta del dia
archivo = zipfile.ZipFile('Proyecto+Dia+9.zip', 'r')

archivo.extractall()"""

"""with open("Instrucciones.txt", "r", encoding="latin-1") as file:
    print(file.read())"""

fecha = datetime.now()

fecha_hoy = fecha.strftime("%d/%m/%y")

ruta = '/Users/felipemartinez/Desktop/pythonProject/Day 9/Mi_Gran_Directorio'

patron_busqueda = r'N+\w{3}+-+\d{4}'


def busqueda(patron):
    conteo = 0
    for carpeta, subcarpeta, archivos in os.walk(ruta):
        for archivo in archivos:
            archivo_path = Path(archivo)

            if archivo_path.suffix == ".txt":
                # Selecciona la primera subcarpeta (si hay alguna) verificar si existe algun archivo, ya que daria error
                subcarpeta_actual = subcarpeta[0] if subcarpeta else ""

                archivo_completo = (Path(carpeta) / subcarpeta_actual / archivo_path).resolve()
                with open(archivo_completo, "r", encoding="latin-1") as file:
                    lectura = file.read()
                    result = re.search(patron, lectura)
                    if result:
                        conteo += 1
                        print(f"{archivo_completo.name}\t{result.group()}")
    print(f"\nNúmeros de coincidencias: {conteo}")


inicio = time.time()
print("_"*50)
print(f"Fecha de búsqueda: {fecha_hoy} \n")
print("ARCHIVO\t\tNRO. SERIE")
print("‾‾‾‾‾‾‾‾\t‾‾‾‾‾‾‾‾‾‾")
busqueda(patron_busqueda)
final = time.time()
resultado = final - inicio
print(f"Duración de la búsqueda: {math.ceil(resultado)} segundos")
print("_"*50)

