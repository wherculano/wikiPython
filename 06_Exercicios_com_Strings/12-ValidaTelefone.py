"""
Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos,
 acrescentando o '3' na frente.
 O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""
tel = input('Telefone: ').replace('-', '')
tam = len(tel)
if tam < 8:
    tel = list(tel)
    digito = '3' * (8 - tam)
    print(f'Telefone possui {tam} dígitos.\nVou acrescentar o(s) digito(s) {digito} na frente.')
    tel.insert(0, digito)
    corrigido = ''.join(tel)
    print(f'Telefone corrigido s/ formatação: {corrigido}')
    tel = corrigido[:4] + '-' + corrigido[4:]
    print(f'Telefone corrigido c/ formatação: {tel}')
else:
    tel = tel[:4] + '-' + tel[4:]
    print(f'Telefone: {tel}')
