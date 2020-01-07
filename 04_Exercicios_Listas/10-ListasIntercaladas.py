"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""
lista_A = [int(input(f'{n + 1}o Numero da lista A: ')) for n in range(10)]

print('-' * 23)

lista_B = [int(input(f'{n + 1}o Numero da lista B: ')) for n in range(10)]

print('-' * 23)

lista_C = []
for a, b in zip(lista_A, lista_B):
    lista_C.append(a)
    lista_C.append(b)

print(lista_C)
