pies= [10, 20, 30, 40, 50]

metros= [p / 3.281 for p in pies]

print(metros)


valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado= [root**2 for root in valores]

print(valores_cuadrado)


valores1 = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares= [par for par in valores1 if par%2 == 0]

print(valores_pares)


temperatura_fahrenheit = [32, 212, 275]

grados_celsius= [(cel - 32)*(5/9) for cel in temperatura_fahrenheit]

print(grados_celsius)