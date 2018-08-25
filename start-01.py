'''Um funcionário de uma empresa recebe, anualmente, aumento salarial.
Sabe-se que:
Esse funcionário foi contratado em 2005 com salário inicial de R$ 1.000,00;
Em 2006 ele recebeu aumento de 1,5% sobre seu salário inicial; e
A partir de 2007, os aumentos salariais sempre corresponderam ao dobro
do percentual do ano anterior.
Faça um algoritmo que determine o salário atual deste funcionário.'''

admissao = 2006
salario_inicial = 1000
reajuste = 1.5

ano_atual = input('Insira aqui o ano em que estamos.\n')
tempo_trabalhado = int(ano_atual) - int(admissao)

for ano in range(0, int(tempo_trabalhado)):
    reajuste_anual = float(ano) * float(reajuste)
    reajuste = reajuste * 2
    reajuste_salarial = (float(salario_inicial) * float(reajuste) / 100 + float(salario_inicial))
print('O salário final do funcinário é R$', reajuste_salarial, ' reais.')
