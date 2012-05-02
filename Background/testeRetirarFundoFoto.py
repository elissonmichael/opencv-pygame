import cv 
import numpy


#Configuracoes :
filtro_de_gauss = 3
tolerancia = 50
filtro_de_dilatacao = 16
filtro_de_erosao = 4


if __name__ == "__main__":

    fundo = cv.LoadImage('fundo.jpg')
    frente = cv.LoadImage('frente.jpg')

    cv.Smooth(fundo,fundo,cv.CV_GAUSSIAN,filtro_de_gauss)
    cv.Smooth(frente,frente,cv.CV_GAUSSIAN,filtro_de_gauss)
    
    mascara = cv.CreateImage(cv.GetSize(frente), 8, 3)
    cinza = cv.CreateImage(cv.GetSize(frente), 8, 1)
    
    #cv.NamedWindow('Fundo',0)
    cv.NamedWindow('Frente',1)
    cv.NamedWindow("Mascara", 1)
    cv.NamedWindow("Cinza", 1)
    cv.NamedWindow("Regiao de Interesse", 1)

    cv.AbsDiff(frente,fundo,mascara)
    cv.CvtColor(mascara, cinza, cv.CV_BGR2GRAY)
    cv.Threshold(cinza,cinza,tolerancia,255,cv.CV_THRESH_BINARY)
   
    cv.Dilate(cinza, cinza, None, filtro_de_dilatacao)
    cv.Erode(cinza, cinza, None, filtro_de_erosao)  

    armazenamento = cv.CreateMemStorage(0)
    contorno = cv.FindContours(cinza, armazenamento, cv.CV_RETR_LIST, cv.CV_LINK_RUNS)
    maiorArea = 0
    listaContornos = []
    listaVertices = []
    quadrante = []
    pixelsbrancos = []
    porcentagem = []

    while contorno:
        
	vertices_do_retangulo = cv.BoundingRect(list(contorno))
	listaVertices.append(vertices_do_retangulo)

	listaContornos.append(cv.ContourArea(contorno))
	maiorArea = max(listaContornos)
	maiorArea_index = listaContornos.index(maiorArea)
	retangulo_de_interesse = listaVertices[maiorArea_index]

	contorno = contorno.h_next()

	cv.SetImageROI(cinza,retangulo_de_interesse)
	regiao_de_interesse = cv.CreateImage((retangulo_de_interesse[2],retangulo_de_interesse[3]), cinza.depth, cinza.channels)
	cv.Copy(cinza,regiao_de_interesse)
	cv.ResetImageROI(cinza)

	ponto1 = (retangulo_de_interesse[0], retangulo_de_interesse[1])
	ponto2 = (retangulo_de_interesse[0] + retangulo_de_interesse[2], retangulo_de_interesse[1] + retangulo_de_interesse[3])
	cv.Rectangle(frente, ponto1, ponto2, cv.CV_RGB(0,0,0), 1)
	#cv.Rectangle(cinza, ponto1, ponto2, cv.CV_RGB(255,255,255), 1)
   	largura = ponto2[0] - ponto1[0]
   	altura = ponto2[1] - ponto1[1]   
   	cv.Line(frente,(ponto1[0]+largura/3,ponto1[1]),(ponto1[0]+largura/3,ponto2[1]), cv.CV_RGB(255,255,255), 1)
   	cv.Line(frente,(ponto1[0]+largura/3+largura/3,ponto1[1]),(ponto1[0]+largura/3+largura/3 ,ponto2[1]), cv.CV_RGB(255,255,255), 1)	    
   	cv.Line(frente,(ponto1[0],ponto1[1]+altura/3),(ponto2[0],ponto1[1]+altura/3), cv.CV_RGB(255,255,255), 1)
   	cv.Line(frente,(ponto1[0],ponto1[1]+altura/3+altura/3),(ponto2[0],ponto1[1]+altura/3+altura/3), cv.CV_RGB(255,255,255), 1)
    
    
    subparte_largura = regiao_de_interesse.width/3
    subparte_altura = regiao_de_interesse.height/3
    area_subparte = subparte_largura*subparte_altura
    for i in range(0,3):
	for j in range (0,3):
		l = 3*i
		retangulo = (subparte_largura*i,subparte_altura*j,subparte_largura,subparte_altura)
		cv.SetImageROI(regiao_de_interesse,retangulo)
		quadrante.append(cv.CreateImage((subparte_largura,subparte_altura), regiao_de_interesse.depth, regiao_de_interesse.channels))
		pixelsbrancos.append(cv.CountNonZero(regiao_de_interesse))
		porcentagem.append(float(pixelsbrancos[l+j])/float(area_subparte))
		print i,j,porcentagem[l+j],pixelsbrancos[l+j]
		cv.Copy(regiao_de_interesse,quadrante[l+j])
		cv.ResetImageROI(regiao_de_interesse)

    print porcentagem

#    cv.ShowImage('Fundo',fundo)
    cv.ShowImage('Frente',frente)
    cv.ShowImage('Mascara',mascara)
    cv.ShowImage('Cinza',cinza)
    cv.ShowImage('Regiao de Interesse',regiao_de_interesse)

    cv.WaitKey(0)
