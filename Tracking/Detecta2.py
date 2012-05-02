import cv
import time

def detecta(imagem):

	imagem_cinza = cv.CreateImage((640,480), 8, 1)
	cv.CvtColor(imagem, imagem_cinza, cv.CV_BGR2GRAY)

	cv.EqualizeHist(imagem_cinza, imagem_cinza)

	armazenamento_rosto = cv.CreateMemStorage(0)
	armazenamento_mao = cv.CreateMemStorage(0)

	padroes_rosto = cv.Load('/home/elisson/OpenCV-2.2.0/data/haarcascades/haarcascade_rosto.xml')
	padroes_mao = cv.Load('/home/elisson/OpenCV-2.2.0/data/haarcascades/haarcascade_mao.xml')


	faces = cv.HaarDetectObjects(imagem_cinza, padroes_rosto, armazenamento_rosto, 1.2, 2, cv.CV_HAAR_FIND_BIGGEST_OBJECT)
	mao = cv.HaarDetectObjects(imagem_cinza, padroes_mao, armazenamento_mao, 1.2, 2, cv.CV_HAAR_FIND_BIGGEST_OBJECT)

	if faces :
		for (x, y, largura, altura),n in faces:
			cv.Rectangle(imagem, ( int(x), int(y)),
				(int(x + largura), int(y + altura)),
				cv.CV_RGB(0, 0, 255), 3, 8, 0)


	if mao :
		for (x, y, largura, altura),n in mao:
			cv.Rectangle(imagem, ( int(x), int(y)),
				(int(x + largura), int(y + altura)),
				cv.CV_RGB(255, 0, 0), 3, 8, 0)

	cv.NamedWindow("Webcam", 1)
	cv.ShowImage("Webcam", imagem)


captura = cv.CaptureFromCAM(1)

while True:

    imagem = cv.QueryFrame(captura)
    cv.Flip(imagem, None, 1)
    detecta(imagem)

    if cv.WaitKey(7) % 0x100 == 27:
        break

