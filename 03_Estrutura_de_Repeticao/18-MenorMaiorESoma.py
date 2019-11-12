"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

while True:
    try:
        n = int(input('Quantos números pretende digitar: '))
        numeros = [int(input(f'{i + 1}º número: ')) for i in range(n)]
        break
    except ValueError:
        print('Valor inválido!')

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)

print(f'\nMenor valor: {menor}')
print(f'Maior valor: {maior}')
print(f'Soma dos valores: {soma}')
