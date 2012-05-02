import pygame, random
from pygame.locals import *
import sys,os

pygame.init()
screen = pygame.display.set_mode([640,480])
mainloop, x,y, color, fontsize, delta, fps =  True, 25 , 0, (32,32,32), 35, 1, 15
clock = pygame.time.Clock()
fundo = pygame.image.load('fundo_branco.png').convert()
parado = pygame.image.load('Standing.png').convert_alpha()
deitado = pygame.image.load('Deitado.png').convert_alpha()

caminhar = []
for i in range(18):
    caminhar.append(pygame.image.load("RunningFastAnimationRight/"+str(i) +".png").convert_alpha())

colidir = []
for i in range(18):
    colidir.append(pygame.image.load("FallAnimationRight/"+str(i) +".png").convert_alpha())

i=0
posicaoX = 0
posicaoY = 260
caiu = False

while mainloop:

    tick_time = clock.tick(fps)
    pygame.display.set_caption("Testando Pygame. FPS: %.2f" % (clock.get_fps()))

    if (caiu == False):
        estado = caminhar[i]
        posicaoX = posicaoX + 10
        if (posicaoX == 500):
            caiu = True
        if (i==17):
            i=0
        else:
            i=i+1

    if (caiu == True):
        estado = colidir[i]
        if (i==17):
           estado = deitado
        else:
            posicaoX = posicaoX - 50
            posicaoY = posicaoY + 45
            i=i+1


    screen.blit(fundo,(0,0))
    screen.blit(estado,(posicaoX,posicaoY))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
    pygame.display.update()

