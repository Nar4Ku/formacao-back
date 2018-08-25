'''Faça um programa para uma loja de tintas. O programa deverá pedir o
tamanho em metros quadrados da área a ser pintada. Considere que a
cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
quantidades de latas de tinta a serem compradas e o preço total.'''
from math import ceil

print('-=' * 25)
print('Calculo de quantidade de tinta/preço')
print('-=' * 25)

area_a_pintar = float(input('Digite o tamanho da área em m² a ser pintada '))  # input da área a ser pintada

cobertura_tinta = area_a_pintar / 3  # calculo da cobertura da tinta

galoes_litro = 18
preco_galao = 80
galoes = ceil(cobertura_tinta / galoes_litro)  # calculo da quantidade de galões
valor = preco_galao * galoes  # calculo do preco final
print('-' * 15)
print(
    'Para pintar {} metros serão necessáios {:.2f} litros de tinta, {} galões e o valor ficará em R$ {:.2f} reais'.format(
        area_a_pintar, cobertura_tinta, galoes, valor))  # printa a quantidade de latasde tinta a serem compradas e o preço total
print('-' * 15)
