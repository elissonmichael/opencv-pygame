import pygame, random
from pygame.locals import *
import sys,os

pygame.init()
screen = pygame.display.set_mode([640,480])
mainloop, x,y, color, fontsize, delta, fps =  True, 25 , 0, (32,32,32), 35, 1, 15
clock = pygame.time.Clock()
fundo = pygame.image.load('fundo_branco.png').convert()
explodir = []
bomba = pygame.image.load('bomba1.png').convert_alpha()
largura_total, altura_total = bomba.get_size()
for i in xrange(int(largura_total/150)):
    explodir.append(bomba.subsurface((i*150,0,150,150)))

i=0
posicaoX = 100
posicaoY = 100

while mainloop:

    tick_time = clock.tick(fps)
    pygame.display.set_caption("Testando Pygame. FPS: %.2f" % (clock.get_fps()))

    screen.blit(fundo,(0,0))
    screen.blit(explodir[i],(posicaoX,posicaoY))

    if i==13:
        i=0
    else:
        i=i+1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
    pygame.display.update()

