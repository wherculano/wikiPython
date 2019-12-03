"""
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

itens = {100: {'nome': 'Cachorro Quente', 'valor': 1.20},
         101: {'nome': 'Bauru Simples', 'valor': 1.30},
         102: {'nome': 'Bauru com Ovo', 'valor': 1.50},
         103: {'nome': 'Hamburguer', 'valor': 1.20},
         104: {'nome': 'CheeseBurguer', 'valor': 1.30},
         105: {'nome': 'Refrigerante', 'valor': 1.00},
         }

pedidos = dict()
total = 0

for k, v in itens.items():
    print(f'{[k]} {v["nome"]:<16} R${v["valor"]:.2f}')

while True:
    while True:
        try:
            pedido, quantidade = list(map(int, input('\nInforme o Nº do Pedido e a Quantidade: ').split()))
            pedidos.update({itens[pedido]["nome"]: itens[pedido]['valor'] * quantidade})
            break
        except (ValueError, KeyError):
            print('Pedido ou Quantidade inválido!\n')

    sair = input('Deseja sair? [S/N]: ').upper()
    if sair == 'S':
        break

print()
for item, valor in pedidos.items():
    print(f'{item:<16} [{quantidade}un] R${valor:.2f}')
    total += valor

print('-'*30)
print(f'Total: {"R$":>18}{total:>4.2f}')
