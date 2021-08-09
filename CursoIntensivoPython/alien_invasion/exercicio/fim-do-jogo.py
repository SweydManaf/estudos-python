"""
13.6 – Fim de jogo:
Usando o código do Exercício 13.5 (Agarando-a-bola),mantenha
o controle do número de vezes que o jogador erra a bola.
Quando ele errar a bola
três vezes, encerre o jogo.
"""
import pygame
from pygame.sprite import Group, Sprite
import sys
from random import randint

class Player(Sprite):
    """Uma representacao do personagem"""
    def __init__(self, *groups):
        super().__init__(*groups)

        # Carregando a imagem e definindo seu rect
        self.image = pygame.image.load("crash_course12-01.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = pygame.Rect(530, 530, 0, 0)

    def update(self, *args):
        """Atualiza o player na tela"""
        # Dicionario que armazena as chaves das teclas!
        keys = pygame.key.get_pressed()

        # Analisa o pressionamento das teclas
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 2
        elif keys[pygame.K_RIGHT] and self.rect.right < 1130:
            self.rect.x += 2

    def centraliza(self):
        """Centraliza o player"""
        self.rect.x = 530

class Bola(Sprite):
    """Representacao da bolinha na tela"""
    def __init__(self, *groups):
        super().__init__(*groups)

        # Carrega a imagem e define o seu rect
        self.image = pygame.image.load("emoji.png")
        self.rect = pygame.Rect(0, 0, 100, 100)

        # Posicionamento inicial
        self.rect.x = randint(0, 1100)

    def update(self, *args):
        """Atualiza a posicao da bola"""
        self.rect.top += 1

        if self.rect.bottom > 700:
            # Elimina a bola caso ela ultrapasse a borda
            self.kill()

class Game_stats:
    """Representa as estatisticas do jogo"""
    def __init__(self, lifes):
        """Inicialiaza os dados estatisticos"""
        self.lifes = lifes

        self.reset_stats()

        # Flag do jogo ativo
        self.game_ativo = True

    def reset_stats(self):
        self.vidas_restantes = self.lifes

def checa_colisao(player, bolas, stats):
    """Responde a colisoes entre o player e a bola"""
    # Remove a bola caso a bola e o player tenham colidido
    collisions = pygame.sprite.spritecollide(player, bolas, True, pygame.sprite.collide_mask)

    for bola in bolas.sprites():
        if bola.rect.y >= 600:
            configura_vidas(player, stats)
            break

def configura_vidas(player, stats):
    from time import sleep
    """Faz a analise das vidas."""
    if stats.vidas_restantes > 0:
        stats.vidas_restantes -= 1
        print(f'VIDAS RESTANTES: {stats.vidas_restantes}')
        sleep(1)
        player.centraliza()
    else:
        stats.game_ativo = False
        print('VOCE PERDEU')


def inicia_jogo():
    """Inicia o jogo"""
    pygame.init()
    tela_largura = 1200
    tela_altura = 600
    janela = [tela_largura, tela_altura]
    tela = pygame.display.set_mode(janela)
    pygame.display.set_caption('Agarando a bola')

    # Armazena todos os objectos
    objectGroup = Group()

    # Cria o player e a bola
    players = Player(objectGroup)
    bolas = Group()

    # Instacia as estatisticas
    stats = Game_stats(3)

    # Laco principal do jogo
    while True:

        # Controla os events da tela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if stats.game_ativo:
            # Cria uma bola caso nao exista nenhuma
            if len(bolas) == 0:
                bola = Bola(objectGroup, bolas)


            # Atualiza a tela a cada passagem
            tela.fill([20, 10, 10])

            players.update()
            bolas.update()

            objectGroup.draw(tela)

            # Checa a colisao da bola e do player
            checa_colisao(players, bolas, stats)

            # Deixa a tela mais recente visivel
            pygame.display.flip()


if __name__ == '__main__':
    inicia_jogo()
