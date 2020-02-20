"""
Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def muda_lados(self, base, altura):
        self.base = base
        self.altura = altura

    def lados(self):
        return f'Base: {self.base}\nAltura: {self.altura}'

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


if __name__ == '__main__':
    largura = float(input('Largura: '))
    altura = float(input('Altura: '))
    ret = Retangulo(largura, altura)
    piso = ret.area()
    print(f'Serão necessarios {piso:.2f}m2 de piso.')
    revest = float(input('Largura do revestimento: '))
    rodape = ret.perimetro() / (revest * 2)
    print(f'Serão necessarias {rodape + 1:.0f} peças de rodape.\n')
