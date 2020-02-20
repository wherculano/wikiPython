"""
Crie uma classe que modele uma bola:
	Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""


class Bola:
    def __init__(self, cor, circ, mat):
        self._cor = cor
        self._circ = circ
        self._material = mat

    def trocaCor(self, cor):
        self._cor = cor

    def mostraCor(self):
        return self._cor


if __name__ == '__main__':
    bola = Bola('azul', 69.5, 'couro')
    print(bola.mostraCor())
    bola.trocaCor('Preta')
    print(bola.mostraCor())
