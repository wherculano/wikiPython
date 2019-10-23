'''
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
"Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

while True:
    turno = input('''Em que turno você estuda?
[M-Matutino, V-Vespertino, N-Noturno]: ''').upper()
    if turno not in 'MNV':
        print('Valor Inválido!\n')
    elif turno == 'M':
        print('Bom Dia!')
        break
    elif turno == 'V':
        print('Boa Tarde!')
        break
    elif turno == 'N':
        print('Boa Noite!')
        break
