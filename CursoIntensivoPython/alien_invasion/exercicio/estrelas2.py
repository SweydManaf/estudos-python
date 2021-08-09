import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from exercicio.config_estrela import Configuracoes
import sys

class Estrela(Sprite):
    """Uma classe que representa uma unica estrela"""
    def __init__(self, config, tela):
        """Inicializa a estrela e define sua posicao inicial."""
        super(Estrela, self).__init__()
        self.config = config
        self.tela = tela

        # Carrega a imagem do alienigena e define seu atributo rect
        self.imagem = pygame.image.load('emoji.png')
        self.rect = self.imagem.get_rect()

        # Inica cada novo estrela a parte superios da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posicao exata da estrela
        self.x = float(self.rect.x)

    def desenha_estrela(self):
        """Desenha a estrela em sua posicao actual"""
        self.tela.blit(self.imagem, self.rect)

def cria_frota(config, tela, estrelas):
    """Cria uma frota completa de estrelas."""
    # Cria uma frota da estrela
    # Cria uma estrela e calucla o numero de estrelas em uma linha
    # O espacamento entre as estrelas e igual a largura de uma estrela
    estrela = Estrela(config, tela)
    estrela_width = estrela.rect.width
    espaco_disponivel = config.tela_largura - 2 * estrela_width
    numero_estrelas_x = int(espaco_disponivel / (2 * estrela_width))

    # Cria a primeira linha de estrelas
    for estrela_numero in range(numero_estrelas_x):
        # Cria uma estrela e o posiciona na linha
        estrela = Estrela(config, tela)
        estrela.x = estrela_width + 2 * estrela_width * estrela_numero
        estrela.rect.x = estrela.x
        estrelas.add(estrela)

def inicia_jogo():
    pygame.init()
    config = Configuracoes()
    tela = pygame.display.set_mode((config.tela_altura,
                                    config.tela_largura))
    pygame.display.set_caption('Estrela')

    estrelas = Group()
    cria_frota(config, tela, estrelas)

    tela.fill(config.cor_fundo)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        estrelas.draw(tela)
        pygame.display.flip()

inicia_jogo()