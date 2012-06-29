import pygame, random
from pygame.locals import *
import sys,os

pygame.init()
screen = pygame.display.set_mode([640,480])
mainloop, x,y, color, fontsize, delta, fps =  True, 25 , 0, (32,32,32), 35, 1, 30
clock = pygame.time.Clock()
fundo = pygame.image.load('fundo_branco.png').convert()
parado = pygame.image.load('standing.png').convert_alpha()

caminhar = []
for i in range(20):
    caminhar.append(pygame.image.load("walk_left/"+str(i) +".png").convert_alpha())

i=0
posicaoX = 100
posicaoY = 160

while mainloop:

    tick_time = clock.tick(fps)
    pygame.display.set_caption("Testando Pygame. FPS: %.2f" % (clock.get_fps()))

    if (i==19):
        i=0
    else:
        i=i+1


    screen.blit(fundo,(0,0))
    screen.blit(caminhar[i],(posicaoX,posicaoY))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
    pygame.display.update()

