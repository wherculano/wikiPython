"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""
dados = [[int(input('\nIdade: ')), float(input('Altura: '))] for _ in range(5)]

print()
for i, a in dados[::-1]:
    print(f'Idade: {i} - Altura: {a}')
