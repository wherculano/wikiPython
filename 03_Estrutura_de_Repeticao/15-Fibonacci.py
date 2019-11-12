"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

while True:
    try:
        n = int(input('n-ésimo Numero: '))
        break
    except ValueError:
        print('Valor Inválido!\n')

ant = 1
prox = 0

for _ in range(n // 2):
    prox += ant
    print(f'{ant}, {prox}', end=', ')
    ant += prox
