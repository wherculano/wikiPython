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

vetor = list(range(1, 10))


def quadrado_magico(lista_de_numeros):
    # tamanho do vetor
    tam = len(lista_de_numeros)
    # nova lista com o tamanho do da variavel vetor
    lista = [0] * tam

    # como o vetor vai de 1 a 9, então a metade vale 5
    # então 5 vai para o meio da variavel lista 5 e será excluida da variavel vetor.
    lista[tam // 2] = lista_de_numeros.pop(lista_de_numeros.index(lista_de_numeros[tam // 2]))

    # listas onde serão guardados os numeros pares e impares
    pares, impares = [], []
    for x, y in enumerate(vetor):
        if y % 2 == 0:
            pares.append(y)
        else:
            impares.append(y)

    def cria_quadrado():
        # variaveis que serão usadas para os indices
        par = 0
        imp = 1

        # união dos conjuntos dos numeros, sendo o conjunto impar em ordem decrescente
        for p, i in zip(pares, reversed(impares)):
            # como o 5 ja está na posição 4, preciso jogar o 6 para a outra posição
            if par == 4:
                par = 6
            lista[par] = p
            lista[imp] = i
            # aqui apenas incremento para que os valores possam ir para as posições corretas
            par += 2
            imp += 2

        def imprime_quadrado_magico():
            for k, v in enumerate(lista, start=1):
                print(v, end=' ')
                if k % 3 == 0:
                    print()

        return imprime_quadrado_magico()

    return cria_quadrado()


quadrado_magico(vetor)
