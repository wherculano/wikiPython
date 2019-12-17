"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
"""

while True:
    try:
        n = int(input('Numero: '))
        break
    except ValueError:
        print('Valor invalido!')

inv_num = str(n)[::-1]
print(f'{"  =>":<8}{inv_num}')
