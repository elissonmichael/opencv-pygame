import cv
import OpenGL
from OpenGL.GLUT import *
from OpenGL.GL import *
from sys import argv

x = 0
y = 0
largura = 0

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
                largura = ((largura*100)/imagem.width)
                #altura = (altura*100)/imagem.height


	cv.NamedWindow("Webcam", 1)
	cv.ShowImage("Webcam", imagem)

def init ():

    glClearColor (255.0, 255.0, 255.0, 0.0)
    glOrtho(-320.0, 320.0, -240.0, 240.0, -1.0, 1.0)

def display():
    print(x,y)
    #if (largura > 16):
     #   print("Cleared Screen ! ")
      #  glClearColor (255.0, 255.0, 0.0, 0.0)
       # glClear(GL_COLOR_BUFFER_BIT)
        #glLoadIdentity()
        #glutSwapBuffers()

    glClear(GL_COLOR_BUFFER_BIT);

    glColor3f (0.0, 0.0, 1.0)
    glPointSize(10.0)
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_BLEND)

    glBegin(GL_POINTS)

    glVertex3fv([x,y,0])


    glutSwapBuffers()


glutInit(argv)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH )
glutInitWindowSize(640, 480)
glutCreateWindow("Testar Motion")
init()
glutDisplayFunc(display)

captura = cv.CaptureFromCAM(1)



while  True:

    imagem = cv.QueryFrame(captura)
    cv.Flip(imagem, None, 1)
    detecta(imagem)
    glutPostRedisplay();
    glutMainLoopEvent();
    if cv.WaitKey(7) % 0x100 == 27:
        break

