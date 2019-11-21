"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
o mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia
seu código, sua altura e seu peso.
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo
 e do mais magro, além da média das alturas e dos pesos dos clientes
"""

clientes = {}
while True:
    while True:
        try:
            cod = int(input('\nCodigo: '))
            break
        except ValueError:
            print('Digite apenas Numeros!')
    if cod == 0:
        break
    else:
        while True:
            try:
                peso = float(input('  Peso: '))
                break
            except ValueError:
                print('Digite apenas números!\n')
        while True:
            try:
                alt = float(input('  Altura: '))
                break
            except ValueError:
                print('Digite apenas números!\n')

        clientes[cod] = {'peso': peso, 'altura': alt}

        # mais alto inicialmente é o primeiro cliente (codigo, altura)
        alto = [list(clientes.keys())[0], clientes[1]['altura']]
        # mais gordo inicialmente é o primeiro cliente (codigo, peso)
        gordo = [list(clientes.keys())[0], clientes[1]['peso']]

soma_pesos = soma_alturas = 0

for k, v in clientes.items():
    soma_pesos += v['peso']
    soma_alturas += v['altura']

    # define quem é o mais alto e mais baixo
    if v['altura'] > alto[1]:
        alto = [k, v['altura']]
    else:
        baixo = [k, v['altura']]

    # define quem é o mais gordo e mais magro
    if v['peso'] > gordo[1]:
        gordo = [k, v['peso']]
    else:
        magro = [k, v['peso']]

media_pesos = soma_pesos / len(clientes)
media_alturas = soma_alturas / len(clientes)

try:
    print(f'Cliente mais Alto -> {alto[0]}: {alto[1]:.2f}')
    print(f'Cliente mais Baixo -> {baixo[0]}: {baixo[1]:.2f}')
    print(f'Cliente mais Magro -> {magro[0]}: {magro[1]:.2f}')
    print(f'Cliente mais Gordo -> {gordo[0]}: {gordo[1]:.2f}')
    print(f'Peso médio: {media_pesos:.2f}')
    print(f'Altura média: {media_alturas:.2f}')
except NameError:
    exit()
