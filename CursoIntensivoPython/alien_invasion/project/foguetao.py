import pygame
from project.configuracoes import Configuracoes

config = Configuracoes()
gameLoop = True
pygame.init()

tela = pygame.display.set_mode((config.tela_altura, config.tela_largura))
pygame.display.set_caption('Preparatorios 01')
tela.fill(config.cor_fundo)

while gameLoop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

    pygame.display.update()
