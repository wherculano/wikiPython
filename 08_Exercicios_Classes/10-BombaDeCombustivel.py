"""
Faça um programa completo utilizando classes e métodos que:

    Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
        tipoCombustivel.
        valorLitro
        quantidadeCombustivel
    Possua no mínimo esses métodos:
        abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi
        colocada no veículo
        abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e
        mostra o valor a ser pago pelo cliente.
        alterarValor( ) – altera o valor do litro do combustível.
        alterarCombustivel( ) – altera o tipo do combustível.
        alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
    OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""


class BombaCombustivel:
    def __init__(self, tipo, valor, qtd):
        self.tipo_combustivel = tipo
        self.valor_litro = valor
        self._quantidade_combustivel = qtd

    @property
    def quantidade_combustivel(self):
        """retorna a quantidade de combustivel na bomba."""
        return f'{self._quantidade_combustivel:.2f}'

    def abastecer_por_valor(self, valor):
        """método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo"""
        qtd = valor / self.valor_litro
        self._quantidade_combustivel -= qtd
        return f'{qtd:.2f}'

    def abastecer_por_litro(self, litro):
        """método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente."""
        qtd = litro * self.valor_litro
        self._quantidade_combustivel -= qtd
        return f'{qtd:.2f}'

    def alterar_valor(self, valor):
        """altera o valor do litro do combustível."""
        self.valor_litro = valor

    def alterar_combustivel(self, tipo):
        """altera o tipo do combustível."""
        self.tipo_combustivel = tipo

    def alterar_quantidade_combustivel(self, qtd):
        """altera a quantidade de combustível restante na bomba."""
        self._quantidade_combustivel = qtd


if __name__ == '__main__':
    bomba = BombaCombustivel('Gasolina', 4.189, 100)
    print(f'Há {bomba.quantidade_combustivel} litros de {bomba.tipo_combustivel} na bomba.\n')
    litro_1 = bomba.abastecer_por_valor(10)
    print(f'Com R$10.00 você abasteceu {litro_1} litros de {bomba.tipo_combustivel}.\n')
    print(f'Há {bomba.quantidade_combustivel} litros de {bomba.tipo_combustivel} na bomba.\n')
    valor_1 = bomba.abastecer_por_litro(2.39)
    print(f'Por 2.39 litros de {bomba.tipo_combustivel}, você pagou R${valor_1}.\n')

    bomba.alterar_valor(3.159)
    bomba.alterar_combustivel('Etanol')
    bomba.alterar_quantidade_combustivel(200)

    print(f'Há {bomba.quantidade_combustivel} litros de {bomba.tipo_combustivel} na bomba.\n')
    litro_2 = bomba.abastecer_por_valor(10)
    print(f'Com R$10.00 você abasteceu {litro_2} litros de {bomba.tipo_combustivel}.\n')
    print(f'Há {bomba.quantidade_combustivel} litros de {bomba.tipo_combustivel} na bomba.\n')

    valor_2 = bomba.abastecer_por_litro(3.17)
    print(f'Por 3.17 litros de {bomba.tipo_combustivel}, você pagaou R${valor_2}.\n')
