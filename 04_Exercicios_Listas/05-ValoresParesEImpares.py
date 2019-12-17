"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

while True:
    try:
        numeros = [int(input(f'{n + 1}º número: ')) for n in range(20)]
        break
    except ValueError:
        print('Valor inválido!')

pares, impares = list(), list()

for n in numeros:
    # fiz essa verificação só para não armazenar valor repetido (apesar de não ter sido pedido)
    if n % 2 == 0 and n not in pares:
        pares.append(n)
    elif n not in impares and n % 2 != 0:
        impares.append(n)

print(f'\nVetor com todos os números:\n{numeros}')
print(f'\nVetor com os números pares:\n{pares}')
print(f'\nVetor com os números ímpares:\n{impares}')
