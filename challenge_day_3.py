text= input("Ingrese el texto a analizar: ").lower()
letter= input('Ingrese las 3 letras a contar en el texto: ').lower()


def assestment(abc, word):
    searching= 'python'
    letters = list(abc)
    the_list = word.split()
    rthe_list= the_list[::-1]
    for l in letters:
        print(f'{l}=', word.count(str(l)))
    print(f'El texto tiene {len(the_list)} palabras')
    print(f"El texto empieza con la letra '{word[0]}' y termina con la letra '{word[-1]}'")
    print(f"El texto empieza con la palabra '{the_list[0]}' y termina con la palabra '{the_list[-1]}'")
    print(f'El texto invertido quedaria de la siguiente manera: {" ".join(rthe_list)}')
    if searching in word:
        print(f'La palabra {searching}, se encuentra en el texto, en la posición {word.index(searching)}')
    else:
        print(f'La palabra {searching}, no se encuentra en el texto')

assestment(letter, text)

