"""
Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um
atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros.
Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%.
Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
"""


class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo


#	@saldo.setter
#	def saldo(self, valor):
#		self._saldo = valor 


class ContaInvestimento:
    def __init__(self, conta, taxa=0):
        self.conta = conta
        self.taxaJuros = taxa

    def adicione_juros(self):
        self.conta._saldo += ((self.taxaJuros / 100) * self.conta.saldo)
        return self.conta._saldo


if __name__ == '__main__':
    poup = ContaBancaria(1000)
    invest = ContaInvestimento(poup, 10)
    for _ in range(5):
        invest.adicione_juros()
    print(poup.saldo)
