"""
Crie uma classe que modele uma pessoa:
Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return f'Nome:{self.nome}\nIdade:{self.idade}\nPeso:{self.peso}kg\nAltura:{self.altura:.2f}cm'

    def __repr__(self):
        return f'Pessoa({self.nome}, {self.idade}, {self.peso}, {self.altura:.2f})'

    def envelhecer(self, ano):
        for i in range(1, ano + 1):
            if self.idade < 21:
                self.crescer(0.05)
            self.idade += 1

    def engordar(self, quilo):
        self.peso += quilo

    def emagrecer(self, quilo):
        self.peso -= quilo

    def crescer(self, tamanho):
        self.altura += tamanho


if __name__ == '__main__':
    wag = Pessoa('Wagner', 18, 81, 1.82)
    print(wag)
    wag.envelhecer(9)
    print('-' * 10)
    wag.emagrecer(10)
    print(wag)
