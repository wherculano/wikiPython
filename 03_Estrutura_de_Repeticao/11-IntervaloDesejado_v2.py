"""
Altere o programa anterior para mostrar no final a soma dos números
"""
soma = 0

while True:
    try:
        ini = int(input('Digite o numero inicial: '))
        break
    except ValueError:
        print('Apenas NUMEROS inteiros!')

while True:
    try:
        fim = int(input('Digite o numero final: '))
        break
    except ValueError:
        print('Apenas NUMEROS inteiros!')

for i in range(ini, fim + 1):
    print(i)
    soma += i

print(f'Soma entre os numeros do intervalo: {soma}')
