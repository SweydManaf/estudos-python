import pygame
from pygame.sprite import Sprite
import sys

class Estrela(Sprite):
    """Uma classe que representa uma unica estrela"""
    def __init__(self, tela, janela):
        """Inicializa a estrela e define sua posicao inicial."""
        super(Estrela, self).__init__()

        self.janela = janela
        self.tela = tela

        # Carrega a imagem do alienigena e define seu atributo rect
        self.imagem = pygame.image.load('emoji.png')
        self.imagem = pygame.transform.scale(self.imagem, [15, 15])
        self.rect = pygame.Rect(0, 0, 0, 0)

        # Inica cada novo estrela a parte superios da tela


        # Armazena a posicao exata da estrela
        self.x = float(self.rect.x)


    def desenha_estrela(self):
        """Desenha a estrela em sua posicao actual"""
        if self.janela[0] > self.rect.x:
            self.rect.x += 30
            self.tela.blit(self.imagem, self.rect)
            print('desenhei x')
        elif self.janela[1] > self.rect.y:
            self.rect.x = 0
            self.rect.y += 30




def inicia_jogo():
    pygame.init()
    tela_altura = 600
    tela_largura = 1200
    janela = (tela_largura, tela_altura)
    tela = pygame.display.set_mode((tela_largura, tela_altura))
    cor = 0, 0, 0
    tela.fill(cor)

    estrela = Estrela(tela, janela)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        estrela.desenha_estrela()
        pygame.display.flip()

inicia_jogo()