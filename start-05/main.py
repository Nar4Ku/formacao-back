'''Crie uma classe para implementar uma conta corrente. A classe deve
possuir os seguintes atributos: número da conta, nome do correntista e
saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No
construtor, saldo é opcional, com valor default zero e os demais atributos
são obrigatórios.'''

from contaCorrente import Conta

correntista_janeiro = Conta(432808822, 'Jonas', 1000)     # setando valores genéricos

correntista_fevereiro = Conta(129767439, 'Lúcia', 2000)

print(type(correntista_janeiro))            # apontando o tipo (classe)
print(correntista_janeiro.correntista)      # indicando o nome do correntista

correntista_janeiro.alterarNome('Juca')     # método de alteração de nome

print(correntista_janeiro.correntista)

print(correntista_fevereiro.saldo)          # indicando o saldo do correntista

correntista_fevereiro.sacar(200)

print(correntista_fevereiro.saldo)          # novo saldo do correntista

print(correntista_janeiro.saldo)            # indicando o saldo do correntista
correntista_janeiro.sacar(1100)             # tentativa de saque
