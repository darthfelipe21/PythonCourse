# Parecido al switch de javascript
cliente= {'nombre': 'Felipe',
          'edad': 38,
          'ocupacion': ['Data Scientist', 'Data Analyst', 'Data Enginer']}

pelicula= {'titulo': 'Interstellar',
           'ficha tecnica': {'director': 'Chirstopher Nolan',
                             'actores': ['Matthew McConaughey',
                                         'Jessica Chastain',
                                         'Anne Hathaway']}}

revision= [cliente, pelicula, 'videojuego']

for r in revision:
    match r:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print('Elemento existe')
            print(f'El elemento tiene los valores de nombre: {nombre}, edad: {edad} y ocupación: {ocupacion}')
        case {'titulo': titulo,
              'ficha tecnica': {'director': director,
                                'actores': actores}}:
            print('Elemento existe')
            print(f'El titulo de la pelicula es {titulo}, dirigida por {director} y cuenta con actores como: {actores}')
        case _:
            print(f'Elemento {r} no existe')

