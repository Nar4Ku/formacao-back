class Conta:                                # criação da classe

    def __init__(self, conta, correntista, saldo):   #set da classe
        self.conta = conta
        self.correntista = correntista
        self.saldo = saldo

    def alterarNome(self, nome_novo):       #método para mudar o nome
        self.correntista = nome_novo

    def deposito(self, depositado):         # método para fazer depósito
        self.saldo += depositado

    def sacar(self, sacar):                 # método para sacar

        if (self.saldo >= sacar):
            self.saldo -= sacar
            return True
        else:
            print('Saldo insuficiente para realizar a operação')
            return False
