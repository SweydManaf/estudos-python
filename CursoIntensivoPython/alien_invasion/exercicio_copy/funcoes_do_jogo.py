import sys
import pygame

def checa_up_eventos(event, espaconave):
    if event.key == pygame.K_UP:
        espaconave.move_cima = False
    elif event.key == pygame.K_DOWN:
        espaconave.move_baixo = False
    elif event.key == pygame.K_RIGHT:
        espaconave.move_direita = False
    elif event.key == pygame.K_LEFT:
        espaconave.move_esquerda = False

def checa_down_eventos(event, espaconave):
    if event.key == pygame.K_UP:
        espaconave.move_cima = True
    elif event.key == pygame.K_DOWN:
        espaconave.move_baixo = True
    elif event.key == pygame.K_RIGHT:
        espaconave.move_direita = True
    elif event.key == pygame.K_LEFT:
        espaconave.move_esquerda = True

def checa_eventos(espaconave):
    """Responde a eventos de posicionamento de teclas e de mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)

        elif event.type == pygame.KEYUP:
            checa_up_eventos(event, espaconave)

        elif event.type == pygame.KEYDOWN:
            checa_down_eventos(event, espaconave)



def atualiza_tela(config, tela, espaconave):
    """Atualiza as imagens na tela e alterna para a nova tela"""
    tela.fill(config.bg_cor)
    espaconave.desenha()

    # Deixa a tela mais recente visivel
    pygame.display.flip()