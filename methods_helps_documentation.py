dic= {'clave1':100, 'clave2': 500}
dic= dic.popitem()
print(dic)

x= ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

print(x.lstrip(',:%_#'))


frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

frutas.insert(3, 'naranja')

print(frutas)


marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados= marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)
