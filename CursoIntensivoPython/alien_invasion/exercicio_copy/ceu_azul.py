import sys
import pygame
from exercicio_copy.configuracoes import Configuracoes
from exercicio_copy.espaconave import Espaconave
import exercicio_copy.funcoes_do_jogo as gf

def inicia_jogo():

    pygame.init()  # inicia o pygame
    config = Configuracoes()
    tela = pygame.display.set_mode(
        (config.tela_largura, config.tela_altura))  # tamanho da tela
    pygame.display.set_caption('Meu primeiro jogo')  # nomeia a janela

    # Cria a espaconave
    espaconave = Espaconave(config, tela)

    #Inicia o laco principal
    while True:

        gf.checa_eventos(espaconave)
        espaconave.update()
        gf.atualiza_tela(config, tela, espaconave)

inicia_jogo()
