# Unir 2 sets
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}

mi_set_3= mi_set_1.union(mi_set_2)

# Como lo set no tienen un orden establecido al usar el metodo pop() elimina un elemento al azar

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

elegido= sorteo.pop()

print(elegido)

# Agregar un elemento a un set

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

sorteo.add('Damián')


"""Los conjunto sets no pueden tener valores repetidos, de hecho al intentar agregar un valor 
 sera descartado repetido, por otra parte los set no pueden estar compuestos por
 listas ni diccionarioa, pero si pueden contener tuplas"""

prueba_set= {1,2,3,(4,5,6,),7,8}

print(prueba_set)

# Eliminar un elemento del set

prueba_set.remove(2)  # Da error si el elemento no existe

print(prueba_set)

prueba_set.discard(1)   # No da error si el elemento no existe

print(prueba_set)


redes = ["YouTube", "Facebook", "Twitter", "Whatsapp"]
print(redes.sort())