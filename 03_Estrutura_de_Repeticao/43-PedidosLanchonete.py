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
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o
cliente deve informar quando o pedido deve ser encerrado.
"""

itens = {100: {'nome': 'Cachorro Quente', 'valor': 1.20},
         101: {'nome': 'Bauru Simples', 'valor': 1.30},
         102: {'nome': 'Bauru com Ovo', 'valor': 1.50},
         103: {'nome': 'Hamburguer', 'valor': 1.20},
         104: {'nome': 'CheeseBurguer', 'valor': 1.30},
         105: {'nome': 'Refrigerante', 'valor': 1.00},
         }

for k, v in itens.items():
    print(f'{[k]} {v["nome"]:<16} R${v["valor"]:.2f}')
