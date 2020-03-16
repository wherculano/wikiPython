"""
Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double).
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário.
Escreva um pequeno programa que teste sua classe.
"""


class Funcionario:
    def __init__(self, nome: str, salario: float):
        self._nome = nome
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def __str__(self):
        return f'\nNome: {self.nome}\nSalario: R${self.salario:.2f}'


wag = Funcionario('Wagner', 5233.19)
print(wag.nome)
print(wag.salario)
print(wag)
