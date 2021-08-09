import pygame
from pygame.sprite import Sprite
import sys

class Estrela(Sprite):
    """Uma classe que representa uma unica estrela"""
    def __init__(self, tela):
        """Inicializa a estrela e define sua posicao inicial."""
        super(Estrela, self).__init__()
        #self.config = config
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

def inicia_jogo():
    pygame.init()
    tela_altura = 1200
    tela_largura = 600
    tela = pygame.display.set_mode((tela_altura, tela_largura))
    cor = 0, 0, 0
    tela.fill(cor)

    estrela = Estrela(tela)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        estrela.desenha_estrela()
        pygame.display.flip()

inicia_jogo()