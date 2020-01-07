"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""
lista_A = [int(input(f'{n + 1}o Numero da lista A: ')) for n in range(10)]

print('-' * 23)

lista_B = [int(input(f'{n + 1}o Numero da lista B: ')) for n in range(10)]

print('-' * 23)

lista_C = [int(input(f'{n + 1}o Numero da lista C: ')) for n in range(10)]

print('-' * 23)

lista_D = []
for a, b, c in zip(lista_A, lista_B, lista_C):
    lista_D.append(a)
    lista_D.append(b)
    lista_D.append(c)

print(lista_D)
