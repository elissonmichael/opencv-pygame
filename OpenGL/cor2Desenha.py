import cv
import OpenGL
from OpenGL.GLUT import *
from OpenGL.GL import *
from sys import argv

x = 0
y = 0

def detectaCor(imagem):
    cv.NamedWindow("Original", 0)
    cv.ShowImage("Original", imagem)
    cv.Smooth(imagem,imagem,cv.CV_GAUSSIAN,3)
    cv.CvtColor(imagem, imagem, cv.CV_BGR2HSV)
    mascara = cv.CreateImage(cv.GetSize(imagem), 8, 1)
    cor_minima = (0, 50, 100)
    cor_maxima = (5, 255, 255)
    cv.InRangeS(imagem, cv.Scalar(*cor_minima), cv.Scalar(*cor_maxima), mascara)

    moments = cv.Moments(mascara, 0)
    area = cv.GetCentralMoment(moments, 0, 0)

    if(area > 10000):
        global x,y
        x = (cv.GetSpatialMoment(moments, 1, 0)/area)/5
        y = (cv.GetSpatialMoment(moments, 0, 1)/area)/5

        #print 'x: ' + str(x) + ' y: ' + str(y) #+ ' area: ' + str(area)
        overlay = cv.CreateImage(cv.GetSize(imagem), 8, 3)
        cv.Add(imagem, overlay, imagem)
        cv.Merge(mascara, None, None, None, imagem)

    cv.CvtColor(imagem, imagem, cv.CV_HSV2BGR)
    #cv.NamedWindow("Resultado", 1)
    #cv.ShowImage("Resultado", imagem)
    cv.NamedWindow("Mascara", 1)
    cv.ShowImage("Mascara", mascara)

def init ():

    glClearColor (255.0, 255.0, 255.0, 0.0)
    glOrtho(-320.0, 320.0, -240.0, 240.0, -1.0, 1.0)

def display():
    #print(x,y)
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
    detectaCor(imagem)
    glutPostRedisplay();
    glutMainLoopEvent();
    if cv.WaitKey(7) % 0x100 == 27:
        break

