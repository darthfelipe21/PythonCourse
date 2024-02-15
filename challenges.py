"""Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valor intermedio."""
def devolver_distintos(x,y,z):
    lista= [x,y,z]
    lista.sort()
    for i in lista:
        if type(i) == str:
            print('Solo se aceptan valores numericos')
        pass
    maximo= max(lista)
    minimo= min(lista)
    mediana= lista[1]
    total = abs(sum(lista))
    if total > 15:
            print(maximo)
    elif total < 10:
            print(minimo)
    elif (total >= 10) and (total <= 15):
            print(mediana)

devolver_distintos(1,3,5)



"""Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como parámetro, y 
que devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.
Por ejemplo si al invocar esta función pasamos la palabra "entretenido", debería devolver 
['d', 'e', 'i', 'n', 'o', 'r', 't']"""

def separar_palabra(word):
    lista= []
    for i in word:
        if i in lista:
            pass
        else:
            lista.append(i)
    lista.sort()
    return lista

prueba= separar_palabra('entretenido')

print(prueba)

""""Escribe una función que requiera una cantidad indefinida de argumentos. Lo que hará esta función es devolver True 
si en algún momento se ha ingresado al numero cero repetido dos veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True (6,0,5,1,0,3,0,1) >>> False"""

def cero_check(*args):
    conteo = 0
    for i in args:
        if i == 0:
            conteo += 1
            if conteo == 2:
                return True
        else:
            conteo = 0
    if conteo != 2:
        return False


test= cero_check(6,0,5,1,0,3,0,1)
test1= cero_check(5,6,1,0,0,9,3,5)
print(test, test1)


"""Escribe una función llamada contar_primos() que requiera un solo argumento numérico.
Esta función va a mostrar en pantalla todos los números primos existentes en el rango que va desde cero 
hasta ese número incluido, y va a devolver la cantidad de números primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos."""

def contar_primos(num):
    primos= [2]  # Se excluye el 2 por ser primo
    conteo= 3
    while conteo <= num:
        for i in range(3, conteo, 2):  # Se va de 2 en 2 para evitar los numeros pares
            if conteo % i == 0:
                conteo += 2   # Se va de 2 en 2 para evitar los numeros pares
                break
        else:
            primos.append(conteo)
            conteo += 2  # Se va de 2 en 2 para evitar los numeros pares
    print(primos)
    print(len(primos))


contar_primos(100)

def numeros_primos(num):
    primos = []
    for i in range(2, num):
        es_primo = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(i)
    return primos

primos = numeros_primos(100)

print(primos)
print(len(primos))

