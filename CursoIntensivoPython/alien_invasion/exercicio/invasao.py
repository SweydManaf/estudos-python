import pygame
from pygame.sprite import Group
from exercicio.configuracoes import Configuracoes
import exercicio.funcoes as gf
from exercicio.espaconave import Espaconave
from exercicio.bala import Bala

def inicia_jogo():
    pygame.init()
    config = Configuracoes()
    tela = pygame.display.set_mode(config.tela)

    pygame.display.set_caption('DISPAROS LATEAIS')

    # Chama a espaconave
    espaconave = Espaconave(config, tela)

    # Chama as balas
    balas = Group()
    while True:
        gf.checa_eventos(config, tela, espaconave, balas)
        espaconave.update()
        balas.update()
        gf.atualiza_balas(balas)
        gf.atualiza_tela(config, tela, espaconave, balas)



inicia_jogo()