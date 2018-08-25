'''Receba o número de horas trabalhadas por uma pessoa e o valor do
salário mínimo e mostre o salário a receber baseado nas seguintes regras:
A hora trabalhada equivale a 10% do salário mínimo informado;
O salário bruto é dado pelo número de horas trabalhadas multiplicado pelo
valor de cada hora;
O imposto pago é de 3%.
O salário a receber é equivalente ao salário bruto subtraído do imposto.'''

print('-='*25)
print('Calculo de salário líquido')
print('-='*25)
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhada '))  #quantidade de horas trabalhadas
piso_salarial = float(input('Digite o valor de seu piso salarial '))         #piso salarial

valor_por_hora = float(piso_salarial/10)        #valor ganho por hora trabalhada

salario_bruto = horas_trabalhadas * valor_por_hora          #sálario bruto
salario_liquido = salario_bruto - salario_bruto * 0.03   # salário com o desconto do imposto

print('-'*15)
print('Salário final será de R$ {:.2f} reais.'.format(salario_liquido))         #printa o salário final com desconto
print('-'*15)
