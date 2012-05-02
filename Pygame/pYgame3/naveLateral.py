import pygame, random
from pygame.locals import *
import sys,os

pygame.init()
screen = pygame.display.set_mode([640,480])
mainloop, x,y, color, fontsize, delta, fps =  True, 25 , 0, (32,32,32), 35, 1, 22
clock = pygame.time.Clock()
fundo = pygame.image.load('fundo.jpg').convert()
fundo2 = pygame.image.load('fundo2.jpg').convert()

posicaoX = - 320
posicaoX2 =  320

while mainloop:

    tick_time = clock.tick(fps)
    pygame.display.set_caption("Testando Pygame. FPS: %.2f" % (clock.get_fps()))

    screen.blit(fundo,(posicaoX,0))
    screen.blit(fundo2,(posicaoX2,0))

    if posicaoX == - 640:
        posicaoX = 640
    else:
        posicaoX = posicaoX - 10

    if posicaoX2 == - 640:
        posicaoX2 = 640
    else:
        posicaoX2 = posicaoX2 - 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
    pygame.display.update()

