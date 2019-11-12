"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
carnes = {
    'File Duplo': 4.90,
    'Alcatra': 5.90,
    'Picanha': 6.90
}

print("""
-> File Duplo
-> Alcatra
-> Picanha
""")

while True:
    while True:
        tipo = input('Tipo de Carne: ').title()
        if tipo in carnes:
            break
        else:
            print('Opcao invalida')
    while True:
        try:
            kg = float(input('Quantos quilos: '))
            break
        except ValueError:
            print('Opcao invalida')

    total = kg * carnes[tipo] if kg <= 5 else kg * (carnes[tipo] + 0.90)

    pagamento = {1: 'Dinheiro', 2: 'Cartao Tabajata'}

    pag = None
    desc = 0
    while True:
        try:
            cart = int(input('\nForma de pagamento:\n[1] - Dinheiro\n[2] - Cartao Tabajara\n[S/N]: '))
            if cart in pagamento:
                pag = pagamento[cart]
                if cart == 2:
                    desc += total * 0.05
                break
            else:
                print('Opcao invalida!')
        except ValueError:
            print('Opcao invalida!')

    print(f'\n{tipo}: {kg:.2f}Kg')
    print(f'Valor: R${total:.2f}')
    print(f'Forma de pagamento: {pag}' if pag != None else '\n')
    print(f'Total de desconto: R${desc:.2f}')
    print(f'Total a pagar: R${total - desc:.2f}')
    break
