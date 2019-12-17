"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = [float(input(f'{i + 1}a Nota: ')) for i in range(4)]

soma = sum(notas)
media = soma / len(notas)

print()
print('NOTAS'.center(15, '-'))
for n in notas:
    print(n, end=' ')

print()
print('MEDIA'.center(15, '-'))
print(f'{media:.2f}')
