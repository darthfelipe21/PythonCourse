# Index, es similar al .find()

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

print(frase.index('práctica'))

print(frase.rindex('práctica'))

frase2 = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

print(frase2[8::3],"\n")

# Invertir cadena
print(frase2[::-1],"\n")

# Mayusculas y minuculas
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper(),"\n")
print(frase.lower(),"\n")

# Unir
lista_palabras = ["La","legibilidad","cuenta."]

print(" ".join(lista_palabras),"\n")

# Reemplazar

x = "Si la implementación es difícil de explicar, puede que sea una mala idea."

word_replacements = {"difícil": "fácil", "mala": "buena"}

for old_word, new_word in word_replacements.items():
    x = x.replace(old_word, new_word)

print(x)

# Capitalizar

cap= "esto es un texto de prueba"
print(cap.capitalize(),"\n")

# Verificar si todos los caracteres son mayusculas o minusculas

test= "abcdefg"

print(test.islower(), test.isupper(),"\n")

# Codificar la cadena con el mapa de caracteres especificado y retorna una instancia del tipo bytes

print(test.encode())

text = "Hola, mundo!"
encoded_text = text.encode(encoding='UTF-8', errors='strict')
print(encoded_text,"\n")

# Contar el numero de apariciones de un valor

print(x.count("i"),"\n")

# Verificar si una cadena empieza o termina con el valor indicado

print(text.startswith('Hola'),"\n")
print(text.endswith('mundo!'),"\n")


# Verificar si una cadena es numerica, es digito, es decimal o si es alfa numerica

number1= "1234.56"
number2= "12345678"

print(number1.isdigit(), number1.isnumeric(), number1.isdecimal(), number1.isalnum(), number1.isalpha())
print(number2.isdigit(), number2.isnumeric(), number2.isdecimal(), number2.isalnum(), number2.isalpha(),"\n")


# Cambiar mayusculas por minisculas y viceversa

mayu_minu= "HoLa, ChAo"

print(mayu_minu.swapcase(),"\n")


# Alinear textos: centro, derecha e izquierda

print("Hola".center(10, "*"))
print("Hola".rjust(10, "*"))
print("Hola".ljust(10, "*"),"\n")


# Remover los espacios en blanca de una cadena

print(" Hola mundo! ".strip())
print(" Hola mundo! ".lstrip())
print(" Hola mundo! ".rstrip())
print("Hola mundo!"[2:].strip('l'),"\n")

# Cortar o dividir una cadena

print("Hola mundo!\nHello world!".split())
print("Hola mundo!\nHello world!".splitlines(),"\n")

# Cortar una cadena y devolver una tupla de 3 elementos, según el separador que se indique

print("Hola mundo. Hello world!".partition(" "))
print("Hola mundo. Hello world!".rpartition(" "),"\n")


# Practicas con strings
x= "Repetición"

print(x*15,"\n")


x="""Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""

print('agua' not in x,"\n")


x="electroencefalografista"

print(len(x),"\n")

# Ordenar
redes = ["YouTube", "Facebook", "Twitter", "Whatsapp"]
redes.sort()  # No se puede asignar a una variable ya que no hara nada

print(redes)



