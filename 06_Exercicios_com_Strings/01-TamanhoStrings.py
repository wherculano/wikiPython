"""
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""
str_1 = input('String 1: ')  # 'Brasil Hexa 2006'
str_2 = input('String 2: ')  # 'Brasil! Hexa 2006!'

tam_1 = len(str_1)
tam_2 = len(str_2)

print('\nCompara duas strings')
print(f'String 1: {str_1}')
print(f'String 2: {str_2}')
print(f'Tamanho de "{str_1}": {tam_1} caracteres')
print(f'Tamanho de "{str_2}": {tam_2} caracteres')
if tam_1 == tam_2:
    print('As duas strings sao de tamanhos iguais.')
else:
    print('As duas strings são de tamanhos diferentes.')
if str_1 == str_2:
    print('As duas strings possuem conteudo iguais.')
else:
    print('As duas strings possuem conteúdo diferentes.')
