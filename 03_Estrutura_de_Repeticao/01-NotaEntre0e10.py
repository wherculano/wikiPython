"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.
"""
while True:
    try:
        nota = float(input('Nota: '))
        if 0 <= nota <= 10:
            break
        else:
            print('Nota invalida')
    except ValueError:
        print('Digite apenas Numeros!')
