"""
/d   Digito         v\d.\d\d     v5.10
/w   Alphanumerico  \w\w\w-\w\w   ABC-10
/s   Espacio Blanco  numero\s\d\d  numero 10
/D   No numerico     \D\D\D\D   AbcD
/W   No alphanumerico \W\W\W   +-*
/S   No espacio blanco \S\S\S  12ac

Caracteres cuantificables

+     1 o mas veces     codigo_\d-\d+    codigo_5-555
{n}   n veces           \d-\d{4}         1-2345
{n,m} de n a m veces     \w{3,5}         hola, to526
{n,}  de n en adelante    -\d{4,}-      -426326-
*     0 o mas veces       \w\s*\w       a2, a   b
?     singular o plural   casas?        casa, casas
"""

import re

texto = "Si necesitas ayuda llama al 658-598-9977 las 24 horas al servicio de ayuda online"

patron = 'ayuda'

busqueda = re.search(patron, texto)

print(busqueda)  # Arroja un objeto con una tupla e indicando el match, la tupla indica de que index a que index va
print(busqueda.span())   # Solo la tupla index
print(busqueda.start())   # De donde empieza index
print(busqueda.end())     # Donde termina index


busqueda2 = re.findall(patron, texto)
print(len(busqueda2))

for i in re.finditer(patron, texto):
    print(i.span())

# Busqueda especial
patron2 = r'\d\d\d-\d\d\d-\d\d\d\d'  # r'\d{3}-\d{3}-\d{4}'

result = re.search(patron2, texto)

print(result)
print(result.group())  # Trae la coincidencia


# Compilar los grupos
patron3 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

result2 = re.search(patron3, texto)

print(result2)
print(result2.group(3))  # No trabaja por index, es el grupo literal


# Cumplir con cierta condición, por ejemplo un password

#contrasena = input('Password: ')

secuencia = r'\D{1}\w{7}'

#revisar = re.search(secuencia, contrasena)

#print(revisar)



mensaje = "No atendemos los lunes por la tarde"

buscar = re.search(r'lunes|martes', mensaje)

print(buscar)


buscar2 = re.search(r'.....demos...', mensaje)

print(buscar2)

# Inicio de frase

buscador = re.search(r'^No', mensaje)

print(buscador)

# Si no existe la busqueda al final

buscador2 = re.search(r'\D$', mensaje)

print(buscador2)



# Verificar un correo electronico
def verificar_email(email):
    patron = r'\w+@\w+.com.\w+|\w+@\w+.com'
    busqueda = re.search(patron, email)
    if busqueda:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

verificar_email('fe@hotmail.com')