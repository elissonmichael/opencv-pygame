import pygame, random
from pygame.locals import *
import cv
import sys,os


def game():
    global posicaoTiro,InimigoVivo,InimigoVivo2,InimigoVivo3,JaMorreu,JaMorreu2,JaMorreu3,FPS_Explosao
    #print y

    tick_time = clock.tick(fps)
    pygame.display.set_caption("Testando Pygame. FPS: %.2f" % (clock.get_fps()))

    screen.blit(fundo,(0,0))
    screen.blit(nave,(x,y))

    if InimigoVivo == False and JaMorreu == False  :
        screen.blit(explodir[FPS_Explosao],(175,5))
        if FPS_Explosao == 13 :
            JaMorreu = True
            FPS_Explosao = 0
        else:
            FPS_Explosao = FPS_Explosao + 1

    if InimigoVivo2 == False and JaMorreu2 == False  :
        screen.blit(explodir[FPS_Explosao],(275,5))
        if FPS_Explosao == 13 :
            JaMorreu2 = True
            FPS_Explosao = 0
        else:
            FPS_Explosao = FPS_Explosao + 1

    if InimigoVivo3 == False and JaMorreu3 == False  :
        screen.blit(explodir[FPS_Explosao],(375,5))
        if FPS_Explosao == 13 :
            JaMorreu3 = True
            FPS_Explosao = 0
        else:
            FPS_Explosao = FPS_Explosao + 1

    if InimigoVivo == True :
        screen.blit(naveInimigo,(200,10))
    if InimigoVivo2 == True :
        screen.blit(naveInimigo2,(300,10))
    if InimigoVivo3 == True :
        screen.blit(naveInimigo3,(400,10))

    screen.blit(tiro,(x + 32,y - 10 + posicaoTiro))

    if posicaoTiro < - 460 :
        posicaoTiro = 0
    else:
        posicaoTiro = posicaoTiro - 30

    if ( x > 170  and x < 230) and (y - 10 + posicaoTiro < 90 ) :
        InimigoVivo = False

    if ( x > 270  and x < 330) and (y - 10 + posicaoTiro < 90 ) :
        InimigoVivo2 = False

    if ( x > 370  and x < 430) and (y - 10 + posicaoTiro < 90 ) :
        InimigoVivo3 = False

    pygame.display.update()


def detecta(imagem):

	imagem_cinza = cv.CreateImage((640,480), 8, 1)
	cv.CvtColor(imagem, imagem_cinza, cv.CV_BGR2GRAY)
	cv.Smooth(imagem_cinza,imagem_cinza,cv.CV_GAUSSIAN,5)
	cv.EqualizeHist(imagem_cinza, imagem_cinza)

	armazenamento = cv.CreateMemStorage(0)

	padroes = cv.Load('/home/elisson/OpenCV-2.2.0/data/haarcascades/haarcascade_mao.xml')

	faces = cv.HaarDetectObjects(imagem_cinza, padroes, armazenamento, 1.2, 2, cv.CV_HAAR_FIND_BIGGEST_OBJECT)
   	if faces :
		for (x, y, largura, altura),n in faces:
			cv.Rectangle(imagem, ( int(x), int(y)),
				(int(x + largura), int(y + altura)),cv.CV_RGB(0, 0, 0), 3, 8, 0)
                global x,y,largura
                x = x + largura
                y = y + altura


	cv.NamedWindow("Webcam", 1)
	cv.ShowImage("Webcam", imagem)

captura = cv.CaptureFromCAM(1)
pygame.init()
screen = pygame.display.set_mode([640,480])
mainloop, x,y, color, fontsize, delta, fps =  True, 25 , 0, (32,32,32), 35, 1, 22
clock = pygame.time.Clock()
fundo = pygame.image.load('fundo.jpg').convert()
nave = pygame.image.load('nave.png').convert_alpha()
tiro = pygame.image.load('tiro.png').convert_alpha()

naveInimigo = pygame.image.load('enemy1.png').convert_alpha()
naveInimigo2 = pygame.image.load('Enemy2.png').convert_alpha()
naveInimigo3 = pygame.image.load('Enemy4.png').convert_alpha()

explodir = []
bomba = pygame.image.load('bomba.png').convert_alpha()
largura_total, altura_total = bomba.get_size()
for i in xrange(int(largura_total/150)):
    explodir.append(bomba.subsurface((i*150,0,150,150)))

posicaoTiro = 0
FPS_Explosao = 0
InimigoVivo = True
InimigoVivo2 = True
InimigoVivo3 = True
JaMorreu = False
JaMorreu2 = False
JaMorreu3 = False

while  True:

    imagem = cv.QueryFrame(captura)
    cv.Flip(imagem, None, 1)
    detecta(imagem)
    game()
    if cv.WaitKey(7) % 0x100 == 27:
        break

