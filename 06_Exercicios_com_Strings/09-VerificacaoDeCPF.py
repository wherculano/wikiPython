"""
Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação
"""

cpf = input('CPF: ').replace('.', '').replace('-', '')

soma_1 = sum([int(n) * i for i, n in zip(list(range(10, 1, -1)), cpf)])

digito_1 = 0 if (soma_1 % 11) < 2 else 11 - (soma_1 % 11)

soma_2 = sum([int(n) * i for i, n in zip(list(range(11, 2, -1)), cpf)]) + (digito_1 * 2)

digito_2 = 0 if (soma_2 % 11) < 2 else 11 - (soma_2 % 11)

digito_final = str(digito_1) + str(digito_2)
if digito_final == cpf[-2:]:
    print('CPF valido!')
else:
    print('CPF invalido!')
