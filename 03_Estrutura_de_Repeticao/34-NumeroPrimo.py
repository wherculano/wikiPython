"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e
determine se ele é ou não um número primo.
"""
while True:
    try:
        num = int(input('Numero: '))
        break
    except ValueError:
        print('Digite apenas números!\n')
div = 1

for i in range(2, num // 2 + 1):
    if num % i == 0:
        div += 1
if div > 1 or num == 1:
    print(f'{num} não é um numero primo.')
else:
    print(f'{num} é um numero primo.')
