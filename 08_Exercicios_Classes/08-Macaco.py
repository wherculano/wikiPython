"""
Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(),
verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com
pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um
macaco coma o outro. É possível criar um macaco canibal?
"""


class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.estomago = []

    def __str__(self):
        return self.nome

    def comer(self, alimento):
        """Alimentar o macaco"""
        if str(alimento) == self.nome:
            print(f'{self.nome} não deveria comer a si próprio!\n')
        else:
            self.estomago.append(alimento)

    def ver_estomago(self):
        """Ver o que tem no estomago"""
        if self.estomago:
            print(f'O {self.nome} ainda tem no estomago:')
            for a in self.estomago:
                print(f' - {a}')
        else:
            print(f'O {self.nome} está com o bucho vazio!\n')

    def digerir(self):
        """Eliminar o que tem no estomago"""
        print(f'\nPronto! a(o) {self.estomago.pop(0)} foi digerida(o)!\n')


if __name__ == '__main__':
    kong = Macaco('Kong')
    print(kong)
    king = Macaco('King')
    kong.comer('banana')
    kong.comer(king)
    kong.ver_estomago()
    kong.digerir()
    kong.ver_estomago()
    kong.digerir()
    kong.ver_estomago()
    print('-' * 20)
    king.comer(kong)
    king.comer(king)
    king.ver_estomago()
