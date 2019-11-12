"""
Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.
"""
while True:
    try:
        ini = int(input('Digite o numero inicial: '))
        break
    except ValueError:
        print('Apenas NUMEROS inteiros!')

while True:
    try:
        fim = int(input('Digite o numero final: '))
        break
    except ValueError:
        print('Apenas NUMEROS inteiros!')

for i in range(ini, fim + 1):
    print(i)
