import pygame
from os import path
import random
import time
import Lenhador

img_dir = path.join(path.dirname(__file__), 'img')
fnt_dir = path.join(path.dirname(__file__), 'font')



WIDTH = 800
HEIGHT = 600



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2



class Player(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        # Carregando a imagem de fundo.
        self.image = pygame.image.load(path.join(img_dir, 'LenhadorE.png')).convert_alpha()
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(self.image, (120, 120))
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH/2 - 30
        self.rect.y = HEIGHT - 100
        #Placar 
        self.pontos = 0
        self.score = 0
        #Posicao do personagem
        self.posicao = 0

    def update(self):
        self.rect.x += self.posicao
        self.pontos += self.score

        if self.rect.right < WIDTH/2 - 30:
            self.rect.right = WIDTH/2 - 30
        if self.rect.left > WIDTH/2 + 30:
            self.rect.left = WIDTH/2 + 30
        self.score = 0


def load_assets(img_dir, fnt_dir):
    assets = {}
    assets["score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    return assets

class Galho(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, posx, posy):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        # Carregando a imagem de fundo.
        self.image = pygame.image.load(path.join(img_dir, 'Galho.png')).convert_alpha()
        # Deiposando transparente.
        self.image.set_colorkey(BLACK)
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

    def update(self):
        #Troca de lado o galho
        if self.rect.x == 200:
            self.image = pygame.image.load(path.join(img_dir, 'GalhoE.png')).convert_alpha()
            self.image.set_colorkey(BLACK)
        else:
            self.image = pygame.image.load(path.join(img_dir, 'GalhoD.png')).convert_alpha()
            self.image.set_colorkey(BLACK)


class Tronco(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        # Carregando a imagem de fundo.
        self.image = pygame.image.load(path.join(img_dir, 'Tronco.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 800))
        # Deiposando transparente.
        self.image.set_colorkey(BLACK)
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.y = 0

    def update(self):
        pass
