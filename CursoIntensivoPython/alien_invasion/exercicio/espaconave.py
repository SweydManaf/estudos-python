import pygame
from exercicio.configuracoes import Configuracoes
class Espaconave:
    """Uma representacao da espaconave no jogo."""
    def __init__(self, config, tela):
        self.config = config
        self.tela = tela

        # Importa a imagem e roda 3 a esquerda
        self.imagem = pygame.image.load('crash_course12-01.png')
        self.imagem = pygame.transform.scale(self.imagem, (60, 60))
        self.imagem = pygame.transform.rotate(self.imagem, 270)

        # Obtem o rectangulo da tela e da imagem
        self.tela_rect = self.tela.get_rect()
        self.rect = self.imagem.get_rect()

        # Posiciona a espaconave na tela
        self.rect.left = self.tela_rect.left
        self.rect.centery = self.tela_rect.centery

        # Flags de movimentos
        self.move_cima = False
        self.move_baixo = False

    def update(self):
        if self.move_cima and self.rect.centery > self.tela_rect.top:
            self.rect.centery -= self.config.valocidade_espaconave
        elif self.move_baixo and self.rect.centery < self.tela_rect.bottom:
            self.rect.centery += self.config.valocidade_espaconave

    def desenha(self):
        self.tela.blit(self.imagem, self.rect)