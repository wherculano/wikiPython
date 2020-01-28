"""
Reverso do número.
Faça uma função que retorne o reverso de um número inteiro informado.
Por exemplo: 127 -> 721.
"""


def inverse_num(num):
    return int(str(num)[::-1])


print(f'127 -> {inverse_num(127)}')
