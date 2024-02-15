import datetime

mi_hora = datetime.time(17, 35, 50, 1500)

print(mi_hora)

fecha = datetime.date(2024, 1, 5)

print(fecha)
print(fecha.ctime())
print(fecha.today())

from datetime import datetime

nueva_fecha = datetime(2024, 1, 15, 22, 30, 15, 1500)
print(nueva_fecha)

nueva_fecha = nueva_fecha.replace(month = 3)

print(nueva_fecha)

from datetime import date

nacimiento = date(1985, 10, 21)
edad = date.today()
resultado = edad - nacimiento

print(resultado.days)


print(datetime.today().minute)