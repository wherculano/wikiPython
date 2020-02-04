"""
Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. 
Esta função deve receber dois parâmetros, linhas e colunas,
sendo que o valor por omissão é o valor mínimo igual a 1e o valor máximo é 20.
Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
"""


def moldura(lin=1, col=20):
    def tam(n):
        n = 1 if n < 1 else n
        n = 20 if n > 20 else n
        return n

    lin = tam(lin)
    col = tam(col)

    for c in range(1):
        print(f'+{"-" * col}+')
        for l in range(lin):
            print(f'|{" " * col}|')
    print('+' + '-' * col + '+')


moldura()
moldura(3, 15)
moldura(-1, 9)  # linha menor
moldura(5, 49)  # coluna maior
moldura(-2, -3)  # ambos errado
