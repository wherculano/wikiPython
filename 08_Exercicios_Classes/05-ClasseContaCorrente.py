"""
Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""


class ContaCorrente:
    def __init__(self, n_conta, nome, saldo=0):
        self.n_conta = n_conta
        self.nome = nome
        self._saldo = saldo

    def __str__(self):
        return f'Conta:{self.n_conta}\nNome:{self.nome}\nSaldo:{self._saldo}'

    def alterar_nome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        self._saldo += valor

    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print(f'Impossivel sacar R${valor}!\nValor superior!\nSeu saldo é de R${self._saldo}.\n')


if __name__ == '__main__':
    conta = ContaCorrente('00018963-0', 'Wagner', 100)
    conta.saldo = 5000
    print(conta)
    print('-' * 20)
    conta.alterar_nome('Wagner Herculano')
    conta.deposito(900)
    conta.saque(1001)
    print('-' * 20)
    print(conta)
    conta.saque(55.89)
    print('-' * 20)
    print(conta)
