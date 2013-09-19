import OpenGL
from OpenGL.GLUT import *
from OpenGL.GL import *
from sys import argv

x = 0
y = 0

def init ():

    glClearColor (255.0, 255.0, 255.0, 0.0)
    glOrtho(-320.0, 320.0, -240.0, 240.0, -1.0, 1.0)

def display():
    global x,y 
    x = x + 1
    y = x + 1

    glClear (GL_COLOR_BUFFER_BIT);
    glColor3f (0.0, 0.0, 0.0)
    glMatrixMode( GL_MODELVIEW )
    glLoadIdentity()
    glPushMatrix()
    glRotatef( x, 0.0, 1.0, 0.0)
    glRotatef( y, 1.0, 0.0, 0.0)
    glutWireSphere( 0.5, 12, 12 )

    glPopMatrix()
    glFlush();

    glutSwapBuffers()


glutInit(argv)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH )
glutInitWindowSize(640, 480)
glutCreateWindow("Testar OpenGL")
init()
glutDisplayFunc(display)

while  True:
    glutPostRedisplay();
    glutMainLoopEvent();


