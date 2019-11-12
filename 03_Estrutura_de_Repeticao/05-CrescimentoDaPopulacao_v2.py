"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""
sair = True

while sair:
    while True:
        try:
            A = float(input('Numero de Habitantes do pais A: '))
            try:
                tx_A = float(input('Taxa de Crescimento do pais A: '))
                break
            except ValueError:
                print('Valor Invalido!')
        except ValueError:
            print('Valor Invalido!')

    while True:
        try:
            B = float(input('\nNumero de Habitantes do pais B: '))
            try:
                tx_B = float(input('Taxa de Crescimento do pais B: '))
                break
            except ValueError:
                print('Valor Invalido!')
        except ValueError:
            print('Valor Invalido!')

    anos = 0
    if A < B and tx_A <= tx_B:
        print('\nA populacao de A nunca sera maior ou igual a B')
    else:
        while B >= A:
            B += B * tx_B / 100
            A += A * tx_A / 100
            anos += 1
        print(
            f'\nEm {anos} anos A tera uma populacao de {A:.2f} habitantes e B tera uma populacao de {B:.2f} habitantes')
    while True:
        try:
            sair = input('\nSair do programa? [S/N]: ').upper()[0]
            if sair == 'S':
                sair = False
            break
        except IndexError:
            print('Opcao invalida!')
