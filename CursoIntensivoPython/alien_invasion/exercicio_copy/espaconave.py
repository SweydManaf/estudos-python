import pygame

class Espaconave:
    def __init__(self,config, tela):
        """Inicializa a espaconave e define sua posicao inicial"""
        self.tela = tela
        self.config = config

        # Carrega a imagem da espaconave e obtem seu rect

        self.imagem = pygame.image.load('crash_course12-01.png')
        self.imagem = pygame.transform.scale(self.imagem, (70, 70))

        self.rect = self.imagem.get_rect()
        self.tela_rect = tela.get_rect()

        # Inicia cada nova espaconave a parte inferior da tela
        self.rect.centerx = self.tela_rect.centerx  # centraliza no eixo x
        self.rect.bottom = self.tela_rect.bottom  # coloca no linha de baixo

        # Flags de movimentos
        self.move_cima = False
        self.move_baixo = False
        self.move_direita = False
        self.move_esquerda = False

    def update(self):
        if self.move_cima and self.rect.bottom != 70:
            self.rect.bottom -= self.config.espaconave_velocidade
        if self.move_baixo and self.rect.bottom != 600:
            self.rect.bottom += self.config.espaconave_velocidade

        if self.move_direita and self.rect.right < self.tela_rect.right:
            self.rect.centerx += self.config.espaconave_velocidade
        if self.move_esquerda and self.rect.left > 0:
            self.rect.centerx -= self.config.espaconave_velocidade

    def desenha(self):
        """Desenha a espaconave em sua posicao actual"""
        self.tela.blit(self.imagem, self.rect)