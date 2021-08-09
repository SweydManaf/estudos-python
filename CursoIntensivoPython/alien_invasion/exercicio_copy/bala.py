import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    """Uma classe que administra balas disparadas pela espaconave"""

    def __init__(self, config, tela, espaconave):
        """Cria um objecto para a bala na posicao actual da
        espaconave"""
        super(Bala, self).__init__()

        self.tela = tela

        # Cria um rectangulo para a bala em (0, 0) e, em seguida
        # define a posicao correta

        self.rect = pygame.Rect(0, 0, config.bala_largura,
                                config.bala_altura)
        self.rect.cetery = espaconave.rect.centery
        self.rect.left = espaconave.rect.left

        # Armazena a posicao do projetil como um valor decimal
        self.x = float(self.rect.x)

        self.cor = config.bala_cor
        self.velocidade = config.bala_velocidade

    def update(self):
        """Move a bala para a esquerda da tela"""
        # Atualiza a posicao decimal do projetil
        self.x -= self.velocidade
        # Atualiza a posicao de rect
        self.rect.left = self.x

    def desenha_bala(self):
        """Desenha a bala na tela"""
        pygame.draw.rect(self.tela, self.cor, self.rect)