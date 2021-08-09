import pygame
import pygame.font
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group


class Alvo(Sprite):
    """Representa um rectangulo na tela"""

    def __init__(self, tela, janela):
        super(Alvo, self).__init__()
        self.tela = tela
        self.janela = janela

        # Obtem os rect necessarios
        self.tela_rect = tela.get_rect()
        self.rect = pygame.Rect([0, 0, 30, 30])
        self.rect.right = self.tela_rect.right
        self.rect.top = self.tela_rect.top

        # Flag
        self.up = True
        self.down = False

        self.velocity_padrao()

    def velocity_padrao(self):
        # Velocidade do alvo
        self.speed_factor = velocidade

    def aumenta_velocidade(self):
        self.speed_factor *= 2

    def update(self):
        """Move o alvo de cima para baixo e vice-versa"""

        if self.up:
            self.rect.y += self.speed_factor
            if self.rect.y >= self.tela_rect.bottom - 30:
                self.up = False
                self.down = True

        elif self.down:
            self.rect.y -= self.speed_factor
            if self.rect.y <= self.tela_rect.top:
                self.up = True
                self.down = False

    def draw(self):
        """Desenha a posicao do alvo."""
        pygame.draw.rect(self.tela, [255, 0, 0], self.rect)


class Espaconave(Sprite):
    """Representa a espaconave na tela."""

    def __init__(self, tela, janela):
        super(Espaconave, self).__init__()
        self.tela = tela
        self.janela = janela

        # Carrega a imagem da espaconave
        self.image = pygame.image.load('crash_course12-01.png')
        self.image = pygame.transform.rotate(self.image, 270)
        self.image = pygame.transform.scale(self.image, [70, 70])
        self.rect = self.image.get_rect()
        self.tela_rect = self.tela.get_rect()

        # Posiciona a espaconave
        self.rect.left = self.tela_rect.left
        self.rect.centery = self.tela_rect.centery

    def update(self):
        """Atualiza a posicao da espaconave."""
        keys = pygame.key.get_pressed()

        # Analisa o pressionamento das teclas
        if keys[pygame.K_UP] and self.rect.y > self.tela_rect.top:
            self.rect.y -= 3
        elif keys[pygame.K_DOWN] and self.rect.y < self.tela_rect.bottom - 70:
            self.rect.y += 3

    def blitme(self):
        """Desenha a espaconve na tela"""
        self.tela.blit(self.image, self.rect)

    def center_ship(self):
        """Centraliza a espaconave."""
        self.rect.centery = self.tela_rect.centery

class Bullet(Sprite):
    """Representacao da bala."""

    def __init__(self, tela, ship):
        super(Bullet, self).__init__()

        self.tela = tela
        self.ship = ship

        # Cria o rect da bala
        self.rect = pygame.Rect(0, 0, 15, 5)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

        # Velocidade da bala
        self.speed = 5

    def update(self, *args):
        """Move o projetil para lado da tela"""
        self.rect.x += self.speed

    def draw_bullet(self):
        """Desenha o projetil na tela."""
        pygame.draw.rect(self.tela, [255, 20, 20], self.rect)


class Button:
    def __init__(self, tela, msg):
        """Inicializa o botao"""
        self.tela = tela
        self.tela_rect = tela.get_rect()

        # Define as dimensoes e as propriedades do botao
        self.largura, self.altura = 200, 50
        self.cor_botao = (0, 0, 255)
        self.cor_texto = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 38)

        # Constroi o objecto rect ao botao e o centraliza
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.center = self.tela_rect.center

        # A mensagem do botao
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Tranforma msg em imagem renderizada e centraliza o texto no botao."""
        self.msg_image = self.font.render(msg, True, self.cor_texto,
                                          self.cor_botao)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Desenha um botao em branco e, em seguida, desenha a mensagem
        self.tela.fill(self.cor_botao, self.rect)
        self.tela.blit(self.msg_image, self.msg_image_rect)

def draw_target(alvos):
    """Desenha o alvo"""
    for alvo in alvos.sprites():
        alvo.draw()
    alvos.update()

def draw_bullet(balas):
    """Desenha as balas"""
    for bala in balas.sprites():
        bala.draw_bullet()
    atualiza_balas(balas)

def disparar(tela, ship, balas):
    """Dispara"""
    if len(balas) < 2:
        nova_bala = Bullet(tela, ship)
        balas.add(nova_bala)


def atualiza_balas(balas):
    """Atualiza a posicao das balas"""
    global cont_failed
    balas.update()
    # Livra-se das balas que desapareceram
    for bala in balas.copy():
        if bala.rect.x >= 800:
            balas.remove(bala)
            cont_failed += 1
            print(cont_failed)


def verifica_colisao(bala, alvo):
    """Verifica colisao entre a bala e o alvo"""
    global velocidade
    colision = pygame.sprite.groupcollide(bala, alvo, True, True)
    if colision:
        velocidade += 0.5


def check_play_button(play_button, mouse_x, mouse_y):
    """Inicia um, novo jogo quando o jogador clicar em Play."""
    clique = play_button.rect.collidepoint(mouse_x, mouse_y)
    if clique:
        return True
    else:
        return False


pygame.init()

largura = 800
altura = 600
janela = [largura, altura]
tela = pygame.display.set_mode(janela)
cor_fundo = [20, 20, 20]
tela.fill(cor_fundo)
pygame.display.set_caption('Treino ao alvo')
time = pygame.time.Clock()

# Rectangulo que sera nosso alvo
alvos = Group()
velocidade = 1
# Espaconave
ship = Espaconave(tela, janela)

# Cria um grupo, no qual serao armazenados as balas
balas = Group()

# Cria o botao play
play_button = Button(tela, 'Play')

# Conta as tentativas
cont_failed = 0

# gameloop
gameloop = False
while True:
    time.tick(120)
    # Analisa os eventos da tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                disparar(tela, ship, balas)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if check_play_button(play_button, mouse_x, mouse_y):
                velocidade = 1
                gameloop = True
                pygame.mouse.set_visible(False)
    # Renova a tinta
    tela.fill(cor_fundo)

    if gameloop:
        # Desenha a espaconve na tela
        ship.blitme()
        ship.update()

        # Desenha e atualiza o alvo na tela
        if len(alvos) == 0:
            new_alvo = Alvo(tela, janela)
            alvos.add(new_alvo)

        # Desenha alvo
        draw_target(alvos)

        # Desenha a bala
        draw_bullet(balas)

        # Verifica a colisao
        verifica_colisao(balas, alvos)
        # Atualiza a tela a cada passagem
    else:
        play_button.draw_button()
        ship.center_ship()

    if cont_failed == 5:
        gameloop = False
        pygame.mouse.set_visible(True)
        cont_failed = 0
        balas.empty()
        alvos.empty()

    pygame.display.flip()
