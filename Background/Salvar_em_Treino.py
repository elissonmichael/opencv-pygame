import cv
import os

#Configuracoes :
filtro_de_gauss = 3
tolerancia = 40
filtro_de_dilatacao = 4
filtro_de_erosao = 2
resolucao_largura = 640
resolucao_altura = 480

captura = cv.CaptureFromCAM(1)
cv.SetCaptureProperty(captura,cv.CV_CAP_PROP_FRAME_WIDTH,resolucao_largura)
cv.SetCaptureProperty(captura,cv.CV_CAP_PROP_FRAME_HEIGHT,resolucao_altura)
cv.NamedWindow("Webcam", 1)
cv.NamedWindow("Mascara", 0)
cv.NamedWindow("Binario", 0)
cv.NamedWindow("Regiao de Interesse", 1)
cv.MoveWindow("Regiao de Interesse",1000,480)
cv.MoveWindow("Mascara",0,500)
cv.MoveWindow("Binario",400,500)

arquivo = open ('Treino.txt','a')

mascara = cv.CreateImage((resolucao_largura,resolucao_altura), 8, 3)
cinza = cv.CreateImage((resolucao_largura,resolucao_altura), 8, 1)


while True:
    print ("Por Favor tire uma foto do fundo estatico do seu video.")
    print ("Aperte a tecla espaco.")
    if cv.WaitKey(0) % 0x100 == 32:
        primeiraImagem = cv.QueryFrame(captura)
        fundo = cv.CloneImage(primeiraImagem)
        cv.Smooth(fundo,fundo,cv.CV_GAUSSIAN,filtro_de_gauss)
        print ("Tirou uma Foto !")
        break
    else:
	print "Uma foto do fundo nao foi tirada" 
	break

while True:

    imagem = cv.QueryFrame(captura)
    cv.Smooth(imagem,imagem,cv.CV_GAUSSIAN,filtro_de_gauss)
    maiorArea = 0
    listaContornos = []
    listaVertices = []
    quadrante = []
    pixelsbrancos = []
    porcentagem = []

    cv.AbsDiff(imagem,fundo,mascara)
    cv.CvtColor(mascara, cinza, cv.CV_BGR2GRAY)
    cv.Threshold(cinza,cinza, tolerancia,255,cv.CV_THRESH_BINARY)

    cv.Dilate(cinza, cinza, None, filtro_de_dilatacao)
    cv.Erode(cinza, cinza, None, filtro_de_erosao)
    regiao_de_interesse = cv.CloneImage(cinza)

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
	cv.SetImageROI(cinza,retangulo_de_interesse)
	global regiao_de_interesse
	regiao_de_interesse = cv.CreateImage((retangulo_de_interesse[2],retangulo_de_interesse[3]), cinza.depth, cinza.channels)
	cv.Copy(cinza,regiao_de_interesse)
	cv.ResetImageROI(cinza)

	ponto1 = (retangulo_de_interesse[0], retangulo_de_interesse[1])
        ponto2 = (retangulo_de_interesse[0] + retangulo_de_interesse[2], retangulo_de_interesse[1] + retangulo_de_interesse[3])
        cv.Rectangle(imagem, ponto1, ponto2, cv.CV_RGB(0,0,0), 2)
        #cv.Rectangle(cinza, ponto1, ponto2, cv.CV_RGB(255,255,255), 1)
        largura = ponto2[0] - ponto1[0]
        altura = ponto2[1] - ponto1[1]
   	cv.Line(imagem,(ponto1[0]+largura/3,ponto1[1]),(ponto1[0]+largura/3,ponto2[1]), cv.CV_RGB(255,255,255), 1)
   	cv.Line(imagem,(ponto1[0]+largura/3+largura/3,ponto1[1]),(ponto1[0]+largura/3+largura/3 ,ponto2[1]), cv.CV_RGB(255,255,255), 1)	    
   	cv.Line(imagem,(ponto1[0],ponto1[1]+altura/3),(ponto2[0],ponto1[1]+altura/3), cv.CV_RGB(255,255,255), 1)
   	cv.Line(imagem,(ponto1[0],ponto1[1]+altura/3+altura/3),(ponto2[0],ponto1[1]+altura/3+altura/3), cv.CV_RGB(255,255,255), 1)
	#x = (640/2-(ponto1[0]+(largura/2)))*-1
	#print x

    subparte_largura = regiao_de_interesse.width/3
    subparte_altura = regiao_de_interesse.height/3
    area_subparte = subparte_largura*subparte_altura
    for i in range(0,3):
	for j in range (0,3):
		l = i*3
		retangulo = (subparte_largura*i,subparte_altura*j,subparte_largura,subparte_altura)
		cv.SetImageROI(regiao_de_interesse,retangulo)
		quadrante.append(cv.CreateImage((subparte_largura,subparte_altura), regiao_de_interesse.depth, regiao_de_interesse.channels))
		pixelsbrancos.append(cv.CountNonZero(regiao_de_interesse))
		porcentagem.append(float(pixelsbrancos[l+j])/float(area_subparte))
		cv.Copy(regiao_de_interesse,quadrante[l+j])
		cv.ResetImageROI(regiao_de_interesse)

    os.system("clear")
    print porcentagem
    #print pixelsbrancos
    
    cv.ShowImage("Mascara", mascara)
    cv.ShowImage("Binario", cinza)
    cv.ShowImage("Webcam", imagem)
    cv.ShowImage('Regiao de Interesse',regiao_de_interesse)

    string_da_lista = str(porcentagem)
    arquivo.write(string_da_lista+'\r\n')

    if cv.WaitKey(7) % 0x100 == 27:
	arquivo.close()
        break

