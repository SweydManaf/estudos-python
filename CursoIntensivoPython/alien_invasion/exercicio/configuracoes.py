class Configuracoes:
    """Prepara as configuracoes do jogo"""
    def __init__(self):

        self.largura = 1200
        self.altura = 600
        self.tela = (self.largura, self.altura)
        self.cor_fundo = (135, 206, 235)
        self.valocidade_espaconave = 2.5

        # COnifiguracoes das balas
        self.bala_largura = 15
        self.bala_altura = 3
        self.bala_cor = (255, 0, 0)
        self.bala_velocidade = 1.5
        self.balas_limite = 5