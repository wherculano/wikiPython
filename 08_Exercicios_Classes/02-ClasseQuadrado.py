"""
Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:
    def __init__(self, lado):
        self._lado = lado

    @property  # get Encapsula e apenas mostra o calor
    def lado(self):
        return self._lado

    @lado.setter  # set Encapsula e possibilita alterar o valor
    def lado(self, valor):
        self._lado = valor

    def area(self):
        return self._lado ** 2


if __name__ == '__main__':
    square = Quadrado(4)
    print(square.lado)
    square.lado = 6
    print(square.lado)
    print(square.area())
