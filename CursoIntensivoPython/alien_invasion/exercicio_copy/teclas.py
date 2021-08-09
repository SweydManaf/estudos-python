import sys
import pygame

pygame.init()
tela = pygame.display.set_mode((1200, 500))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(event.key)

    pygame.display.flip()
