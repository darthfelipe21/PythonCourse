dic= {'c1':[1,2,3], 'c2':['a','b','c']}

dic['c3']= [5,6,7]

dic['c4']= {'saludo':'hola', 'despedida':'chao'}

print(dic['c2'][0].upper())

print(dic['c4']['saludo'])

print(dic)

dic['c1'][0]= 'cambio'

print(dic)

print(dic.keys())

print(dic.values())
print(dic.items())


mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic['ocupacion'], mi_dic['edad'], mi_dic['pais']= 'Editora', 36, 'Colombia'