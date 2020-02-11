"""
Um quadrado mágico é aquele dividido em linhas e colunas,
com um número em cada posição e no qual a soma das linhas,colunas e diagonais é a mesma.
Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4 
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
"""

from itertools import permutations


def test_magic_square(array):
    """
    Verifica se as combinações são iguais a 15
    """
    if len(array) != 9:
        return False

    # Lines
    for i in range(0, 7, 3):
        if sum(array[i:i + 3]) != 15:
            return False

    # Columns
    for i in range(3):
        if sum(array[i::3]) != 15:
            return False

    # Diagonal 1
    for i in range(3):
        if sum(array[::4]) != 15:
            return False

    # Diagonal 2
    for i in range(3):
        if sum(array[2:8:2]) != 15:
            return False
    return True


def show_magic_square(combinations):
    """
    printa todas as combinações
    """
    cont = 1
    for items in combinations:
        print(f' {cont}a COMBINACAO '.center(21, '#'))
        for i in range(0, 7, 3):
            print(*items[i:i + 3])
        print()
        cont += 1


# Fazer permutação entre a quantidade de números do range. 9 neste caso (1,2,3,4,5,6,7,8,9) (1,3,5,6,2,7,4,9,8)...
# Se desejar fazer combinação de 2 numeros por exemplo, usar permutations(range(10), 2)
vector = permutations(range(1, 10))

magic_square = []
for array in vector:
    if test_magic_square(array):
        magic_square.append(array)

show_magic_square(magic_square)
