import pygame
from os import path
import random
import time
from Lenhador import Tronco
from Lenhador import Player
from Lenhador import Galho
from Lenhador import load_assets
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


VIDA = 10

GALHO_LISTA = [(450, HEIGHT - 120),
               (200, HEIGHT - 270),
               (200, HEIGHT - 420),
               (450, HEIGHT - 570),
               (450, HEIGHT - 720)]

background = pygame.image.load(path.join(img_dir, 'fundo.jpg'))
background = pygame.transform.scale(background, (800, 600))
background_rect = background.get_rect()

imginicio = pygame.image.load(path.join(img_dir, 'Tela de inicio.png'))
imginicio = pygame.transform.scale(imginicio, (800, 600))
imgfundo_rect = imginicio.get_rect()

# Inicialização do Pygame.
pygame.init()

# Carrega todos os assets uma vez só e guarda em um dicionário
assets = load_assets(img_dir, fnt_dir)
score_font = assets["score_font"]

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Lumberjack")


all_sprites = pygame.sprite.Group()
galho = pygame.sprite.Group()

## Cria as sprites. O construtor será chamado automaticamente.
tronco = Tronco()
player = Player()
all_sprites.add(tronco)
all_sprites.add(player)

#Pego da internet 
font = pygame.font.SysFont("C:\Windows\Fonts\Arial.ttf", 72)
text = font.render("Pontos: {0}".format(player.pontos), True, YELLOW)
textRect = text.get_rect()
textRect.center = (WIDTH // 2 - 300, 50)
####
#Pego da internet
for branch in GALHO_LISTA:
    g = Galho(*branch)
    all_sprites.add(g)
    galho.add(g)
####
try:
    
    running = True
    main = True

    while main:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                main = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    main = False

        screen.fill(BLACK)
        screen.blit(imginicio, imgfundo_rect)
        pygame.display.flip()

    while running:

        #clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            #Ação
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.posicao = 170
                    player.image = pygame.image.load(path.join(img_dir, 'LenhadorD.png')).convert_alpha()
            
                if event.key == pygame.K_LEFT:
                    player.posicao = -220
                    player.image = pygame.image.load(path.join(img_dir, 'LenhadorE.png')).convert_alpha()
                    player.image = pygame.transform.scale(player.image, (120, 120))

                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:       
                    player.score = 1
                    text = font.render("Pontos: {0}".format(player.pontos), True, YELLOW)
                    textRect = text.get_rect()
                    textRect.center = (WIDTH // 2 - 300, 50)

                    for branch in galho:
                        branch.rect.y += 100
                        if branch.rect.top >= HEIGHT:
                            branch.kill()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.posicao = 0
                    player.image = pygame.image.load(path.join(img_dir, 'LenhadorE.png')).convert_alpha()
                    player.image = pygame.transform.scale(player.image, (120, 120))

                if event.key == pygame.K_RIGHT:
                    player.posicao= 0
                    player.image = pygame.image.load(path.join(img_dir, 'LenhadorD.png')).convert_alpha()
                    player.image = pygame.transform.scale(player.image, (120, 120))

        #Pego da da internet
        if len(galho) < 4:
            lista_posicao = [200, 450]
            random.shuffle(lista_posicao)
            g = Galho(lista_posicao[0], 40)
            all_sprites.add(g)
            galho.add(g)
        
        

        if VIDA <= 0:
            running = False

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, galho, False,pygame.sprite.collide_mask)
        if hits:
            VIDA-=1
            print("PONTOS: ", player.pontos-1)
            running = False
            
        

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        screen.blit(text, textRect)
        all_sprites.draw(screen)

        #Desenha os corações
        text_surface = score_font.render(chr(9829) * VIDA, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (WIDTH/2-100, HEIGHT - 530)
        screen.blit(text_surface, text_rect)
        
        pygame.display.flip()


finally:
    pygame.quit()
