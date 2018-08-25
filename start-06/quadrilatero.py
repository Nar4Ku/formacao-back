class Quadrilatero:

    def __init__(self, comprimento, largura, comprimento_area, largura_area):
        self.comprimento = comprimento
        self.largura = largura
        self.comprimento_area = comprimento_area
        self.largura_area = largura_area

    def seta_lados(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def retornaLados(self):
        print("O comprimento é de {} e a largura é de {}".format(self.comprimento, self.largura))

    def calc_perimetro(self):
        print("O perímetro  de {} m".format((self.comprimento * 2) + (self.largura * 2)))

    def calc_area(self):
        return self.comprimento * self.largura

    def medida_espaco(self):
        return self.comprimento_area * self.largura_area

    def calculo(self):
        medida_piso = customer.calc_area()
        area = customer.medida_espaco()
        print("Será necessário {:.2f}cm² de piso".format(medida_piso, area))
