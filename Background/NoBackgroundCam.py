import cv

captura = cv.CaptureFromCAM(0)
maiorArea = 0

#cv.NamedWindow("Fundo", 0)
cv.NamedWindow("Webcam", 1)
cv.NamedWindow("Mascara", 0)
cv.NamedWindow("Cinza", 1)


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

while True:

    imagem = cv.QueryFrame(captura)
    cv.Smooth(imagem,imagem,cv.CV_GAUSSIAN,3)
    
    cv.AbsDiff(imagem,fundo,mascara)
    cv.CvtColor(mascara, cinza, cv.CV_BGR2GRAY)
    cv.Threshold(cinza,cinza, 50,255,cv.CV_THRESH_BINARY)
    
    cv.Dilate(cinza, cinza, None, 18)
    cv.Erode(cinza, cinza, None, 10) 

    armazenamento = cv.CreateMemStorage(0)
    contorno = cv.FindContours(cinza, armazenamento, cv.CV_RETR_LIST, cv.CV_LINK_RUNS)
    
    while contorno:
	vertices_do_retangulo = cv.BoundingRect(list(contorno))
	if (cv.ContourArea(contorno)> maiorArea):
		maiorArea = cv.ContourArea(contorno)
		retangulo_de_interesse = vertices_do_retangulo

	ponto1 = (retangulo_de_interesse[0], retangulo_de_interesse[1])
        ponto2 = (retangulo_de_interesse[0] + retangulo_de_interesse[2], retangulo_de_interesse[1] + retangulo_de_interesse[3])
        cv.Rectangle(imagem, ponto1, ponto2, cv.CV_RGB(0,0,0), 2)
        cv.Rectangle(cinza, ponto1, ponto2, cv.CV_RGB(255,255,255), 1)
        largura = ponto2[0] - ponto1[0]
        altura = ponto2[1] - ponto1[1]
        cv.Line(cinza,(ponto1[0]+largura/2,ponto1[1]),(ponto1[0]+largura/2,ponto2[1]), cv.CV_RGB(255,255,255), 1)
        cv.Line(cinza,(ponto1[0],ponto1[1]+altura/2),(ponto2[0],ponto1[1]+altura/2), cv.CV_RGB(255,255,255), 1)

        contorno = contorno.h_next()

    cv.ShowImage("Mascara", mascara)
    cv.ShowImage("Cinza", cinza)
    
    cv.ShowImage("Webcam", imagem)
    #cv.ShowImage("Fundo", fundo)
    
    if cv.WaitKey(7) % 0x100 == 27:
        break

