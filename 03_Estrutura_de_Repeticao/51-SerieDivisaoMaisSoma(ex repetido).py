"""
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
"""
dividendo = divisor = 1
s = 0
n = int(input('Numero: '))

for i in range(n):
    print(f'{dividendo}/{divisor}', end='')
    s += dividendo / divisor
    if i == (n - 1):
        print(' = ', end='')
        print(s)
    else:
        print(' + ', end='')
    dividendo += 1
    divisor += 2
