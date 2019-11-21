"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões)
"""

while True:
    try:
        n = int(input('Numero: '))
        aux = n
        if n < 0:
            n *= -1
        break
    except ValueError:
        print('Valor invalido!\n')

primos = []
cont = 1

for i in range(1, n + 1):
    div = 0
    for d in range(2, int(i // 2) + 1):
        cont += 1
        if i % d == 0:
            div += 1
    if div < 1:
        primos.append(i)

for p in primos:
    print(p, end=', ')
print(f'\nForam efetuadas {cont} divisoes.')
