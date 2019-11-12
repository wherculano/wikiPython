"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

while True:
    try:
        n = int(input('Quantidade de Números que serão digitados: '))
        if n == 0:
            n = 1
        break
    except ValueError:
        print('Valor Inválido!\n')

numeros = []

for i in range(n):
    while True:
        try:
            num = int(input(f'{i + 1}º Numero: '))
            if 0 < num <= 1000:
                numeros.append(num)
                break
            else:
                print('Digite um número valido [0-1000]\n')
        except ValueError:
            print('Valor Invalido!\n')

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)

print(f'\nMenor valor: {menor}')
print(f'Maior valor: {maior}')
print(f'Soma dos valores: {soma}')
