import pygame, random
from pygame.locals import *
import sys,os

pygame.init()
screen = pygame.display.set_mode([640,480])
mainloop, x,y, color, fontsize, delta, fps =  True, 25 , 0, (32,32,32), 35, 1, 15
clock = pygame.time.Clock()
fundo = pygame.image.load('fundo_branco.png').convert()
parado = pygame.image.load('parado.png').convert()
caminhar = []
sequencia_andar = pygame.image.load('andar_sequencia.png').convert_alpha()
master_width, master_height = sequencia_andar.get_size()
for i in xrange(int(master_width/82)):
    caminhar.append(sequencia_andar.subsurface((i*82,0,82,119)))

i=0
posicaoX = 0

while mainloop:

    tick_time = clock.tick(fps)
    pygame.display.set_caption("Testando Pygame. FPS: %.2f" % (clock.get_fps()))

    if (posicaoX < 300):
        estado = caminhar[i]
        posicaoX = posicaoX + 5

        if (i==7):
            i=0
        else:
            i=i+1
    if posicaoX == 300:
        estado = parado



    screen.blit(fundo,(0,0))
    screen.blit(estado,(posicaoX,360))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
    pygame.display.update()

