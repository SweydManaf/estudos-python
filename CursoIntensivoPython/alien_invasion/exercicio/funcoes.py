import pygame
import sys
from exercicio.bala import Bala

def dispara(config, tela, espaconave, balas):
    """Dispara um projetil se o limite ainda nao foi alcancado."""
    # Cria um novo projetil e o adiciona ao grupo de projeteis
    if len(balas) < config.balas_limite:
        nova_bala = Bala(config, tela, espaconave)
        balas.add(nova_bala)

def checa_eventos(config, tela, espaconave, balas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit('Volte sempre...')

        elif event.type == pygame.KEYDOWN:
            """Ouve os pressionamentos das teclas"""
            if event.key == pygame.K_UP:
                espaconave.move_cima = True
            elif event.key == pygame.K_DOWN:
                espaconave.move_baixo = True
            elif event.key == pygame.K_SPACE:
                dispara(config, tela, espaconave, balas)


        elif event.type == pygame.KEYUP:
            """Responde a solturas das teclas"""
            if event.key == pygame.K_UP:
                espaconave.move_cima = False
            elif event.key == pygame.K_DOWN:
                espaconave.move_baixo = False

def atualiza_tela(config, tela, espaconave, balas):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laco
    tela.fill(config.cor_fundo)
    # Redesenha todos os projeteis atras da espaconave e dos alienigenas
    for bala in balas.sprites():
        bala.desenha_bala()
    espaconave.desenha()

    # Deixa a tela mais recente visivel
    pygame.display.flip()

def atualiza_balas(balas):
    """Atualiza a posicao dos projeteis"""
    balas.update()

    # Livra-se dos projeteis que desapareceram
    for bala in balas.copy():
        if bala.rect.x >= 1200:
            balas.remove(bala)

