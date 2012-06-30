import pygame, random
from pygame.locals import *
import sys,os

pygame.init()
screen = pygame.display.set_mode([640,480])
mainloop, x,y, color, fontsize, delta, fps =  True, 25 , 0, (32,32,32), 35, 1, 30
clock = pygame.time.Clock()
fundo = pygame.image.load('fundo.jpg').convert()
parado = pygame.image.load('standing.png').convert_alpha()

levantar_ambos_os_bracos = []
levantar_braco_direito = []
levantar_braco_esquerdo = []
caminhar_direita = []
caminhar_esquerda = []

for i in range(0,29):
    levantar_ambos_os_bracos.append(pygame.image.load("both_arms/"+str(i) +".png").convert_alpha())
    levantar_braco_direito.append(pygame.image.load("right_arm/"+str(i) +".png").convert_alpha())
    levantar_braco_esquerdo.append(pygame.image.load("left_arm/"+str(i) +".png").convert_alpha())
    caminhar_direita.append(pygame.image.load("walk_right/"+str(i) +".png").convert_alpha())
    caminhar_esquerda..append(pygame.image.load("walk_left/"+str(i) +".png").convert_alpha())



i=0
posicaoX = 100
posicaoY = 160

while mainloop:

    tick_time = clock.tick(fps)
    pygame.display.set_caption("Testando Pygame. FPS: %.2f" % (clock.get_fps()))

    if (i==28):
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

