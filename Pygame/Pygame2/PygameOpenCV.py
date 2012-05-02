import pygame, random
from pygame.locals import *
import cv
import sys,os
x = 0
y = 0
i = 0

def game():
    global i,estado,posicaoX,posicaoY
    print(x,y)

    if (x > 120):
        if(posicaoY == 360):
            estado = caminharDireita[i]
            if (i == 7):
                i = 0
            else:
                i = i + 1
                posicaoX = posicaoX + 3

    if (x < -120):
        if(posicaoY == 360):
            estado = caminharEsquerda[i]
            if (i == 0):
                i = 7
            else:
                i = i - 1
                posicaoX = posicaoX - 3

    if ((x > -120)and(x < 120)):
        if(posicaoY == 360):
            estado = paradoDireita

    if ((posicaoY == 360)and(y > 125)):
        estado = puloDireita
        posicaoY = posicaoY - 68


    tick_time = clock.tick(fps)
    pygame.display.set_caption("Testando Pygame. FPS: %.2f" % (clock.get_fps()))
    #pygame.display.set_caption("Testando Pygame")
    screen.blit(fundo,(0,0))
    screen.blit(estado,(posicaoX,posicaoY))
    pygame.display.update()
    if (posicaoY < 360) :
        posicaoY = posicaoY + 4

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
				(int(x + largura), int(y + altura)),
				cv.CV_RGB(0, 0, 255), 3, 8, 0)
                global x,y
                x = ((imagem.width/2-(x+(largura/2)))*-1)
                y = -((imagem.height/2-(y+(altura/2)))*-1)


	cv.NamedWindow("Webcam", 1)
	cv.ShowImage("Webcam", imagem)




posicaoX = 300
posicaoY = 360
captura = cv.CaptureFromCAM(1)
pygame.init()
screen = pygame.display.set_mode([640,480])
mainloop, x,y, color, fontsize, delta, fps =  True, 25 , 0, (32,32,32), 35, 1, 20
clock = pygame.time.Clock()
fundo = pygame.image.load('fundo_branco.png').convert()
paradoDireita = pygame.image.load('parado.png').convert_alpha()
puloDireita = pygame.image.load('pulo.png').convert_alpha()
paradoEsquerda = pygame.image.load('parado2.png').convert_alpha()
caminharDireita = []
caminharEsquerda = []
sequencia_andar_direita = pygame.image.load('andar_sequencia.png').convert_alpha()
sequencia_andar_esquerda = pygame.image.load('andar_sequencia2.png').convert_alpha()
master_width, master_height = sequencia_andar_direita.get_size()
master_width, master_height = sequencia_andar_esquerda.get_size()
for i in xrange(int(master_width/82)):
    caminharDireita.append(sequencia_andar_direita.subsurface((i*82,0,82,119)))
    caminharEsquerda.append(sequencia_andar_esquerda.subsurface((i*82,0,82,119)))
estado = paradoDireita

while  True:

    imagem = cv.QueryFrame(captura)
    cv.Flip(imagem, None, 1)
    detecta(imagem)
    game()
    if cv.WaitKey(7) % 0x100 == 27:
        break

