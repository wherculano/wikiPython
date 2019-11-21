"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
fatorial a números inteiros positivos e menores que 16.
"""

while True:
    while True:
        try:
            fat = int(input('Fatorial de: '))
            if fat <= 16:
                break
            else:
                print('[ERRO]: Digite um numero menor ou igual a 16!\n')
        except ValueError:
            print('Valor Invalido!\n')

    fatorial = 1

    print(f'{fat}!=', end='')
    for f in range(fat, 0, -1):
        fatorial *= f
        print(f, end='')
        if f == 1:
            print('=', end='')
        else:
            print('.', end='')

    print(fatorial)

    sair = input('\nDeseja encerrar o programa? [S/N]: ').lower()
    if sair == 's':
        break
