import pygame, random
from pygame.locals import *
import sys,os

pygame.init()
screen = pygame.display.set_mode([640,480])
mainloop, x,y, color, fontsize, delta, fps =  True, 25 , 0, (32,32,32), 35, 1, 20
clock = pygame.time.Clock()
fundo = pygame.image.load('fundo.jpg').convert()
naveJogador = pygame.image.load('nave.png').convert_alpha()
naveInimigo = pygame.image.load('enemy1.png').convert_alpha()
tiro = pygame.image.load('tiro.png').convert_alpha()

retangulo_tiro = tiro.get_rect()
retangulo_naveInimigo = naveInimigo.get_rect()

explodir = []
bomba = pygame.image.load('bomba.png').convert_alpha()
largura_total, altura_total = bomba.get_size()
for i in xrange(int(largura_total/150)):
    explodir.append(bomba.subsurface((i*150,0,150,150)))

posicaoTiro = 0

posicaoX = 250
posicaoY = 390

retangulo_tiro.move(posicaoX + 32,posicaoY - 10 + posicaoTiro)
retangulo_naveInimigo.move(250,10)

FPS_Explosao = 0
InimigoVivo = True
JaMorreu = False


while mainloop:

    tick_time = clock.tick(fps)
    pygame.display.set_caption("Testando Pygame. FPS: %.2f" % (clock.get_fps()))

    screen.blit(fundo,(0,0))

    if InimigoVivo == False and JaMorreu == False  :
        screen.blit(explodir[FPS_Explosao],(225,5))
        if FPS_Explosao == 13 :
            JaMorreu = True
        else:
            FPS_Explosao = FPS_Explosao + 1

    if InimigoVivo == True :
        screen.blit(naveInimigo,(250,10))

    screen.blit(naveJogador,(posicaoX,posicaoY))

    screen.blit(tiro,(posicaoX + 32,posicaoY - 10 + posicaoTiro))
    retangulo_tiro.move(posicaoX + 32,posicaoY - 10 + posicaoTiro)

    if posicaoTiro < -460 :
        posicaoTiro = 0
    else:
        posicaoTiro = posicaoTiro - 15

    #print retangulo_tiro.colliderect(retangulo_naveInimigo)
    if posicaoTiro < -320 : InimigoVivo = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
    pygame.display.update()

