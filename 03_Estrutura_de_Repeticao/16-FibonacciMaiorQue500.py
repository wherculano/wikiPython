"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
"""

ant = 1
prox = 0

while True:
    prox += ant
    print(f'{ant}, {prox}', end=', ')
    ant += prox
    if ant >= 610:
        break
