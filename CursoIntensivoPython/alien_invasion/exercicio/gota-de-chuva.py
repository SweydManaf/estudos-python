import pygame
from pygame.sprite import Sprite, Group
import sys

class Chuva(Sprite):
    def __init__(self, tela, janela):
        super(Chuva, self).__init__()
        self.screen = tela
        self.janela = janela

        # Carrega a imagem da gota e define seu rect
        self.image = pygame.image.load('emoji.png')
        self.rect = self.image.get_rect()

        # Inicia cada gota proxima a parte superior da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self, *args):
        """Move a gota para baixo"""
        self.rect.y += 1


    def blitme(self):
        """Desenha a gota na posicao actual."""
        self.screen.blit(self.image, self.rect)

def get_number_coluna(janela, chuva_height):
    """Determina o numero de linhas com gotas que cabem na tela."""
    availble_space_y = (janela[1] - (3 * chuva_height))
    number_coluna = int(availble_space_y / (2 * chuva_height))
    return number_coluna

def cria_gota(janela, tela, chuva, gota_number, coluna_number):
    """ Cria uma gota e o posiciona na linha"""
    gota = Chuva(tela, janela)
    gota_width = gota.rect.width
    gota.x = gota_width + 2 * gota_width * gota_number
    gota.rect.x = gota.x
    gota.rect.y = gota.rect.height + 2 * gota.rect.height * coluna_number
    chuva.add(gota)

def cria_frota(janela, tela, gotas):
    """Cria uma frota completa de gotas."""
    # Cria uma gota e calcula o numero de gotas em uma linha
    # O espacamento entre as gotas e igual a largura de uma gota
    gota = Chuva(tela, janela)
    gota_width = gota.rect.width
    available_space_x = janela[0] - 2 * gota_width
    number_gotas_x = int(available_space_x / (2 * gota_width))
    number_coluna = get_number_coluna(janela, gota.rect.height)

    # Cria a primeira linha de gotas
    for coluna_number in range(number_coluna):
        for gota_number in range(number_gotas_x):
            #Cria uma gota e o posiciona na linha
            cria_gota(janela, tela, gotas, gota_number, coluna_number)

def update_gotas(janela, gotas):
    """Atualiza as posicoes de todas gotas da frota"""
    gotas.update()


def inicia_jogo():
    # Inicializa o jogo e cria um objecto para a tela
    pygame.init()
    tela_largura = 1200
    tela_altura = 600
    janela = (tela_largura, tela_altura)
    tela = pygame.display.set_mode((tela_largura, tela_altura))
    pygame.display.set_caption('Chuva')

    # Cria um grupo de gotas
    chuva = Group()
    cria_frota(janela, tela, chuva)
    # Inicia o laco principal do jogo
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        update_gotas(janela, chuva)

        # Atualiza as imagens na tela e alterna para a nova tela
        tela.fill((0, 200, 10))
        chuva.draw(tela)

        # deixa a tela mais recente visivel
        pygame.display.flip()

inicia_jogo()