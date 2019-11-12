"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
    nome = input('Nome: ')
    if len(nome) > 3:
        break
    else:
        print('Nome precisa ter mais de 3 letras!')

while True:
    try:
        idade = int(input('Idade: '))
    except ValueError:
        print('Valor invalido')
    else:
        if 0 <= idade <= 150:
            break

while True:
    try:
        salario = float(input('Salario: R$'))
    except ValueError:
        print('Valor Invalido!')
    else:
        if salario >= 0:
            break

while True:
    sexo = input('[M/F]: ').lower()
    if sexo in 'mf' and sexo != '':
        break

while True:
    try:
        est_civ = input('Estado Civil: ').lower()[0]
        if '' != est_civ in 'scvd':
            break
    except IndexError:
        print('Valor Invalido!')
