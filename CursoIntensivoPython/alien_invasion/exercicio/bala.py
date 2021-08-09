import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    """Uma representacao dos projeteis que a espaconave vai lancar"""
    def __init__(self, config, tela, espaconave):
        """Cria um objecto para o projetil na posicao actual"""
        super(Bala, self).__init__()
        self.tela = tela

        # Cria um rectangulo para a bala em (0, 0) e, em seguida
        # define a posicao correta
        self.rect = pygame.Rect(0, 0, config.bala_largura,
                                config.bala_altura)
        self.rect.centery = espaconave.rect.centery
        self.rect.right = espaconave.rect.right

        self.cor = config.bala_cor
        self.velocidade = config.bala_velocidade


    def update(self):
        """Move o projetil para direita da tela"""

        self.rect.x += self.velocidade

    def desenha_bala(self):
        """Desenha a bala na tela"""
        pygame.draw.rect(self.tela, self.cor, self.rect)
