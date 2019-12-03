"""
Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.
"""
numeros = []
while True:
    try:
        num = float(input('Numero: '))
        if num >= 0:
            numeros.append(num)
        else:
            break
    except ValueError:
        print('Numero Invalido!\n')

"""
gera uma lista filtrada com os numeros do intervalo determinado pela funcao lambda.
E depois pega o tamanho dessa lista.
"""
for i in range(25, 101, 25):
    # (x > i - 25 and x < i + 1)
    print(f'{len(list(filter(lambda x: i - 25 < x < i + 1, numeros)))} numeros no intervalo de {[i - 24, i]}')
