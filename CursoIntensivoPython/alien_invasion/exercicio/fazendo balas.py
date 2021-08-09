import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    """Uma classe que administra projeteis disparadados pela
    espaconave"""

    def __init__(self, config, tela, objecto):
        """Cria um objecto pra o projetil na posicao actual
        da espaconave"""
        super(Bala, self).__init__()
        self.tela = tela

        # Cria um rectangulo para o projectil em (0, 0) e, em seguida,
        # define a posicao correta

        self.rect = pygame.Rect(0, 0, config.bala_largura,
                                config.bala_altura)
        # 'posObject' - posicao do objecto principal
        self.rect.posObject = objecto.rect.posObject
        # 'posDirecao' - posicao da direcao da bala
        self.rect.posDirecao = objecto.rect.posObject

        self.cor = config.bala_cor
        self.velocidade = config.bala_velocidade

    def update(self):
        """Move a bala para a direcao informada."""
        # Atualiza a posicao da bala
        # cord_direcao - varia de x ou y depende da direcao informada
        self.rect.cord_direcao += self.velocidade

    def desenha_bala(self):
        """Desenha a bala na tela"""
        pygame.draw.rect(self.tela, self.cor, self.rect)

#####################################################################
################## Ficheiro principal ################################
######################################################################

import pygame
from pygame.sprite import Group

# Cria um grupo, no qual serao armazenadas as balas
balas = Group()

# dentro do laco principal inserir os comandos
# caso exista um game fuctions
gf.checa_eventos(config, tela, objecto, balas)
balas.update()
gf.update_balas()
for bala in balas.sprites():
    bala.desenha_bala()
gf.update_tela(config, tela, objecto, balas)


#####################################################################
#################### Game fuctions ##################################
####################################################################
from bala import Bala

# no checa eventos down-comando inserir a linha seguinte
disparar(config, tela, objecto, balas)

# na funcao disparar
def disparar(config, tela, objecto, balas):
    """Dispara um projetil se o limite ainda nao foi alcancado."""
    if len(balas) < config.balas_limietes:
        nova_bala = Bala(config, tela, objecto)
        balas.add(nova_bala)

# na funcao atualiza balas
def atualiza_balas(balas):
    """Atualiza a posicao das balas"""
    balas.update()

    # Livra-se das balas que desapareceram
    for bala in balas.copy():
        # posInicial - saida da bala
        # 0 - valor que define onde a bala sera apagada
        if bala.rect.posInicial <= 0:
            balas.remove(bala)


