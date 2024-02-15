num1= 36
num2= 72/2
num3= 48

mi_bool1= (num1 > num2) and (num1 < num3)

print(mi_bool1)

num1= 36
num2= 72/2  # 36
num3= 48

mi_bool2= (num1 > num2) or (num1 < num3)

print(mi_bool2)

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool3=  not ((palabra1 in frase) and (palabra2 in frase))

print(mi_bool3)