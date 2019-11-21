"""
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados
também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
"""

while True:
    try:
        num = int(input('Montar a Tabuada de: '))
        break
    except ValueError:
        print('Digite apenas números!\n')

while True:
    while True:
        try:
            ini = int(input('Começar por: '))
            break
        except ValueError:
            print('Digite apenas números!\n')
    while True:
        try:
            fim = int(input('Terminar em: '))
            break
        except ValueError:
            print('Digite apenas números!\n')

    if ini < fim:
        break
    else:
        print('O inicio nao pode ser maior que o final!\n')

for t in range(ini, fim + 1):
    print(f'{num} x {t} = {num * t}')
