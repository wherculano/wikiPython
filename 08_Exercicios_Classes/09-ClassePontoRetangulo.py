"""
Faça um programa completo utilizando funções e classes que:

    1- Possua uma classe chamada Ponto, com os atributos x e y.
    2- Possua uma classe chamada Retangulo, com os atributos largura e altura.
    3- Possua uma função para imprimir os valores da classe Ponto
    4- Possua uma função para encontrar o centro de um Retângulo.
    5- Você deve criar alguns objetos da classe Retangulo.
    6- Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo,
    que deve ser um objeto da classe Ponto.
    7- A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique
    os valores de x e y para o centro do objeto.
    8- O valor do centro do objeto deve ser mostrado na tela
    9- Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""


class Ponto:  # 1
    def __init__(self, px=0.0, py=0.0):
        self.x = px
        self.y = py

    def __str__(self):
        return f'{self.x, self.y}'  # 8

    def valores(self):  # 3
        return self.x, self.y


class Retangulo:  # 2
    def __init__(self, base=0.0, altura=0.0, ponto=Ponto()):
        self.largura = base
        self.altura = altura
        self.vertice_de_partida = ponto  # 6

    def __str__(self):
        return f'{self.largura, self.altura}'

    def centro(self):  # 4
        vert_x = self.vertice_de_partida.x + self.largura / 2
        vert_y = self.vertice_de_partida.y + self.altura / 2
        return Ponto(vert_x, vert_y)  # 7


if __name__ == '__main__':
    def alterar_valores(obj):  # 9
        while True:
            try:
                obj.largura = float(input('Base: '))
                obj.altura = float(input('Altura: '))
                obj.vertice_de_partida.x = float(input('Vértice X: '))
                obj.vertice_de_partida.y = float(input('Vértice Y: '))
                break
            except ValueError:
                print('Você digitou algum valor inválido. Digite apenas números.\n')


    while True:  # 9
        ponto = Ponto(10, 25)
        x, y = ponto.valores()
        retangulo = Retangulo(x, y)  # 5
        print(retangulo.centro())  # 8

        sair = input('\nDeseja Sair? [S/N]: ').upper()
        if sair == 'S':
            break
        else:
            alterar_valores(retangulo)
