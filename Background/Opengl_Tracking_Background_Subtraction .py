import OpenGL
import cv
from OpenGL.GLUT import *
from OpenGL.GL import *
from sys import argv

resolucao_largura = 640
resolucao_altura = 480
x = 0

def detecta(imagem):

    cv.Smooth(imagem,imagem,cv.CV_GAUSSIAN,3)
    maiorArea = 0
    listaContornos = []
    listaVertices = []

    cv.AbsDiff(imagem,fundo,mascara)
    cv.CvtColor(mascara, cinza, cv.CV_BGR2GRAY)
    cv.Threshold(cinza,cinza, 50,255,cv.CV_THRESH_BINARY)

    cv.Dilate(cinza, cinza, None, 18)
    cv.Erode(cinza, cinza, None, 18) 

    armazenamento = cv.CreateMemStorage(0)
    contorno = cv.FindContours(cinza, armazenamento, cv.CV_RETR_LIST, cv.CV_LINK_RUNS)
    
    while contorno:
        vertices_do_retangulo = cv.BoundingRect(list(contorno))
	listaVertices.append(vertices_do_retangulo)

	listaContornos.append(cv.ContourArea(contorno))
	maiorArea = max(listaContornos)
	maiorArea_index = listaContornos.index(maiorArea)
	retangulo_de_interesse = listaVertices[maiorArea_index]

	contorno = contorno.h_next()

	ponto1 = (retangulo_de_interesse[0], retangulo_de_interesse[1])
        ponto2 = (retangulo_de_interesse[0] + retangulo_de_interesse[2], retangulo_de_interesse[1] + retangulo_de_interesse[3])
        cv.Rectangle(imagem, ponto1, ponto2, cv.CV_RGB(0,0,0), 2)
        cv.Rectangle(cinza, ponto1, ponto2, cv.CV_RGB(255,255,255), 1)
        largura = ponto2[0] - ponto1[0]
        altura = ponto2[1] - ponto1[1]
        cv.Line(cinza,(ponto1[0]+largura/2,ponto1[1]),(ponto1[0]+largura/2,ponto2[1]), cv.CV_RGB(255,255,255), 1)
        cv.Line(cinza,(ponto1[0],ponto1[1]+altura/2),(ponto2[0],ponto1[1]+altura/2), cv.CV_RGB(255,255,255), 1)
	global x
	x = ((640/2-(ponto1[0]+(largura/2)))*-1)/5


    cv.ShowImage("Webcam", imagem)
    cv.ShowImage("Mascara", mascara)
    cv.ShowImage("Cinza", cinza)


def init ():

    glClearColor (0.0, 0.0, 0.0, 0.0)
    glOrtho(-320.0, 320.0, -240.0, 240.0, -1.0, 1.0)

def display():
    print(x)
    glClear (GL_COLOR_BUFFER_BIT);

    glColor3f (1.0, 1.0, 0.0)

    glMatrixMode( GL_MODELVIEW )
    glLoadIdentity()
    glPushMatrix()
    glRotatef( x, 0.0, 1.0, 0.0)
    glutWireSphere( 0.5, 12, 12 )

    glPopMatrix()
    glFlush();

    glutSwapBuffers()


glutInit(argv)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH )
glutInitWindowSize(640, 480)
glutCreateWindow("Testar Background Subtraction Motion")
init()
glutDisplayFunc(display)

captura = cv.CaptureFromCAM(0)
cv.SetCaptureProperty(captura,cv.CV_CAP_PROP_FRAME_WIDTH,resolucao_largura)
cv.SetCaptureProperty(captura,cv.CV_CAP_PROP_FRAME_HEIGHT,resolucao_altura)
cv.NamedWindow("Webcam", 1)
cv.NamedWindow("Mascara", 0)
cv.NamedWindow("Cinza", 0)
mascara = cv.CreateImage((640,480), 8, 3)
cinza = cv.CreateImage((640,480), 8, 1)

while True:
    print ("Por Favor tire uma foto do fundo estatico do seu video.")
    print ("Aperte a tecla espaco.")
    if cv.WaitKey(0) % 0x100 == 32:
        primeiraImagem = cv.QueryFrame(captura)
        fundo = cv.CloneImage(primeiraImagem)
        cv.Smooth(fundo,fundo,cv.CV_GAUSSIAN,3)
        print ("Tirou uma Foto !")
        break

while  True:
    imagem = cv.QueryFrame(captura)
    #cv.Flip(imagem, None, 1)
    detecta(imagem)
    glutPostRedisplay();
    glutMainLoopEvent();
    if cv.WaitKey(7) % 0x100 == 27:
        break

