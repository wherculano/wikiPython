"""
Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas.
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador terá seis tentativas para adivinhar a palavra.
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
"""

from random import shuffle, choice

palavras = ['wagner', 'python', 'github', 'android', 'programacao']

escolhida = choice(palavras)
emb_escolhida = list(escolhida)
shuffle(emb_escolhida)
# shuffle(emb_escolhida)
cont = 1

while cont < 7:
    print(''.join(emb_escolhida))
    chute = input('Qual é a palavra acima?\nResp.: ')
    if chute == escolhida:
        print('Acertou!!')
        break
    else:
        print(f'\nErrado!\nVoce ainda tem {6 - cont} chances!\n')
        cont += 1
print(f'\nA palavra correta era: {escolhida}')
