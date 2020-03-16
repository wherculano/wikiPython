"""
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o
salário do funcionário em uma certa porcentagem.
Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)
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

    def aumentarSalario(self, perc):
        self._salario += (perc / 100 * self.salario)
        return self.salario


harry = Funcionario("Harry", 25000)
print(harry.salario)
harry.aumentarSalario(10)
print(harry.salario)
