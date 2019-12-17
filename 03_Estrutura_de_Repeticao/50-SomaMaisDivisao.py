"""
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
"""
H = 1
s = 0
n = int(input('Numero: '))
print(f'{H}', end=' + ')
for i in range(2, n + 2):
    print(f'{H}/{i}', end='')
    s += H / i
    if i == (n + 1):
        H = s
        print(f' = {H}')
    else:
        print(' + ', end='')
