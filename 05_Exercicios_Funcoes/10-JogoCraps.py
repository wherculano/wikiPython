"""
Faça um programa de implemente um jogo de Craps.
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
eu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""
from random import randint
from time import sleep


def lançar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    print(f'Dado 1 = {dado1}\nDado 2 = {dado2}\nSoma dos dados = {dado1 + dado2}\n')
    return dado1 + dado2


primeira_jogada = lançar_dados()
if primeira_jogada == 7 or primeira_jogada == 11:
    print('Você Ganhou!')
elif primeira_jogada == 2 or primeira_jogada == 3 or primeira_jogada == 12:
    print('CRAPS! Você perdeu!')
else:
    print('Ponto')
    while True:
        sleep(0.9)
        proxima_jogada = lançar_dados()
        if proxima_jogada == 7:
            print('Você Perdeu!')
            break
