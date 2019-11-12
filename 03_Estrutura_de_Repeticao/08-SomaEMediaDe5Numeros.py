"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
while True:
    try:
        numeros = [int(input(f'{i + 1}o numero: ')) for i in range(5)]
        break
    except ValueError:
        print('\nDigite apenas numeros!')

soma = sum(numeros)
media = soma / len(numeros)

print(f'\nSoma entre todos os numeros: {soma}')
print(f'Media entre todos os numeros: {media}')
