import pygame, random
from pygame.locals import *
class pixel:
   def __init__(self,screen):
       self.screen = screen
       self.Xscreen ,self.Yscreen = self.screen.get_size()
       self.x = random.randint(0,self.Xscreen)
       self.y = 0
       self.speed = 1

   def Update(self):

       #red = random.randint(0,255)
       if (random.randint(0,1))==1:
            green = random.randint(0,255)
       else:
        green =0
       #blue = random.randint(0,255)

       if self.y < self.Yscreen:
           self.y += self.speed
       else:
           self.y = 0
           self.x = random.randint(0,self.Xscreen)
       self.screen.set_at((self.x, self.y), (0, green,0 ))

def Game():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Demo')
    screen = pygame.display.set_mode((800,480))
    exit = False
    pixels =[]
    i=0
    while i <=400 :
        i+=1
        x=pixel(screen)
        x.speed = random.randint(0,10)
        pixels.append(x)
    while not exit:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit = True
        for pix in pixels:
            pix.Update()

        pygame.display.flip()
        pygame.time.wait(50)

# This starts the game loop.
Game()

pygame.quit()

