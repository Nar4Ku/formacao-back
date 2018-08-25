'''Crie uma classe que modele um retângulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a
escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e
calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que
informe as medidas de um local. Depois, deve criar um objeto com as medidas
 e calcular a quantidade de pisos e de rodapés necessárias para o
local.'''
from quadrilatero import Quadrilatero

comprimento_piso = float(input("Insira a medida do comprimento do piso em centímetros"))
largura_piso = float(input("Insira a medida da largura do piso em centímetros"))
comprimento_area = float(input("Insira o comprimento da área  em centímentros onde colocará os pisos"))
largura_area = float(input("Insira a largura da área  em centímentros onde colocará os pisos"))

customer = Quadrilatero(comprimento_piso, largura_piso, comprimento_area, largura_area)
customer.calculo()
