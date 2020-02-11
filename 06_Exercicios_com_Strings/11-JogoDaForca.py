"""
Desenvolva um jogo da forca.
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""
from random import choice

erros = 1

palavras = ['texto', 'python', 'programaçao', 'exercicio', 'inteligente', 'desenvolvedor', 'logica']

escolhida = choice(palavras)
forca = ['_'] * len(escolhida)

while erros < 7:
    letra = input('\nDigite uma letra: ').lower()
    if letra in escolhida:
        for i, l in enumerate(escolhida):
            if l == letra:
                forca[i] = l
        print(f'A palavra é:', *forca)
        if forca == list(escolhida):
            print('FIM DE JOGO'.center(20, '#'))
            break
    else:
        print(f'\nVocê errou pela {erros}a vez. Tente de novo!\n')
        erros += 1
