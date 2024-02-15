numero = 10

while numero >= 0:
    print(numero)
    numero -= 1


print(10*'*')

numeros = 50

while numeros >= 0:
    if numeros%5 == 0:
        print(numeros)
        numeros -= 1
    else:
        numeros -= 1

print(10*'*')

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for positive in lista_numeros:
    if positive > 0:
        print(positive)
    else:
        break

"""
-Si el código llega a una instrucción BREAK, se produce la salida del bucle.
-La instrucción CONTINUE interrumpe la iteración actual dentro del bucle, 
llevando al programa a la parte superior del bucle.
-La instrucción PASS no altera el programa: ocupa un lugar donde se espera 
una declaración, pero no se desea realizar una acción.
"""