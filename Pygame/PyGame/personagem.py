import pygame, random
from pygame.locals import *
import sys,os

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images, fps = 10):
        pygame.sprite.Sprite.__init__(self)
        self._images = images

        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = 0

        self.update(pygame.time.get_ticks())

    def update(self, t):

        if t - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self._images): self._frame = 0
            self.image = self._images[self._frame]
            self._last_update = t

def Game():

    posicaoX = 0

    pygame.init()
    pygame.display.set_caption(' Primeiro Teste ')
    tela = pygame.display.set_mode((640,480))
    tela = pygame.Surface(tela.get_size())
    tela = tela.convert()
    tela.fill((255,0,255))

    caminhar = []
    sequencia_andar = pygame.image.load('andar_sequencia.png').convert_alpha()
    master_width, master_height = sequencia_andar.get_size()
    for i in xrange(int(master_width/82)):
        caminhar.append(sequencia_andar.subsurface((i*82,0,82,119)))


    andar = AnimatedSprite(caminhar)


    #andando = AnimatedSprite(caminhar)
    #personagem = pygame.image.load('parado.png').convert_alpha()

    #tela.blit(caminhar[2],(posicaoX,360))
    andar.update(10)
    andar.draw(tela)
    pygame.display.flip()
    while True:
        eventos = pygame.event.get()

        for evento in eventos:
            if evento.type in (QUIT, KEYDOWN):
                if evento.key == K_SPACE:
                    posicaoX += 10
                    #tela.blit(personagem,(posicaoX,360))
                    #pygame.display.flip()
                if evento.key == K_ESCAPE:
                    print('Elisson Michael [UENF] : Projeto de IC ')
                    sys.exit(0)


Game()

pygame.quit()

