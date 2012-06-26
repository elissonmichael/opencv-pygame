import cv
from numpy import array
from scipy.cluster.vq import vq
from os import system
from Code_Book import code_book
from Treino_HMM import *
from ghmm import *

#Configuracoes :
divisoes_para_vetor_de_caracteristicas = 6
tolerancia = 30
filtro_de_gauss = 3
filtro_de_dilatacao = 2
filtro_de_erosao = 2
resolucao_largura = 640
resolucao_altura = 480

video = cv.CaptureFromFile('videos/testar_todos.avi')
frames_total = int( cv.GetCaptureProperty( video, cv.CV_CAP_PROP_FRAME_COUNT ) )
fps = cv.GetCaptureProperty( video, cv.CV_CAP_PROP_FPS )
waitPerFrameInMillisec = int( 1/fps * 1000/1 )

cv.NamedWindow("Video", 0)
cv.NamedWindow("Mascara", 1)
#cv.NamedWindow("Binario", 1)
cv.MoveWindow("Video",1000,510)
cv.MoveWindow("Mascara",0,0)
#cv.MoveWindow("Binario",650,0)
cv.NamedWindow("Regiao de Interesse", 1)
cv.MoveWindow("Regiao de Interesse",650,0)

mascara = cv.CreateImage((resolucao_largura,resolucao_altura), 8, 3)
cinza = cv.CreateImage((resolucao_largura,resolucao_altura), 8, 1)
fundo = cv.LoadImage('videos/fundo.jpg')
cv.Smooth(fundo,fundo,cv.CV_GAUSSIAN,filtro_de_gauss)

simbolos = []
probabilidades = []

for f in xrange( frames_total ):
    system('clear')

    imagem = cv.QueryFrame(video)
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
	largura = ponto2[0] - ponto1[0]
	altura = ponto2[1] - ponto1[1]
	cv.Rectangle(mascara, ponto1, ponto2, cv.CV_RGB(255,255,255), 1)
	ponto_largura = largura/divisoes_para_vetor_de_caracteristicas
	ponto_altura = altura/divisoes_para_vetor_de_caracteristicas

	for i in range(1,divisoes_para_vetor_de_caracteristicas):
		cv.Line(mascara,(ponto1[0]+ponto_largura*i,ponto1[1]),(ponto1[0]+ponto_largura*i,ponto2[1]), cv.CV_RGB(255,255,255), 1)
		cv.Line(mascara,(ponto1[0],ponto1[1]+ponto_altura*i),(ponto2[0],ponto1[1]+ponto_altura*i), cv.CV_RGB(255,255,255), 1)

    subparte_largura = regiao_de_interesse.width/divisoes_para_vetor_de_caracteristicas
    subparte_altura = regiao_de_interesse.height/divisoes_para_vetor_de_caracteristicas
    area_subparte = subparte_largura*subparte_altura

    for i in range(0,divisoes_para_vetor_de_caracteristicas):
	for j in range (0,divisoes_para_vetor_de_caracteristicas):
		l = i*divisoes_para_vetor_de_caracteristicas
		retangulo = (subparte_largura*i,subparte_altura*j,subparte_largura,subparte_altura)
		cv.SetImageROI(regiao_de_interesse,retangulo)
		quadrante.append(cv.CreateImage((subparte_largura,subparte_altura), regiao_de_interesse.depth, regiao_de_interesse.channels))
		pixelsbrancos.append(cv.CountNonZero(regiao_de_interesse))
		if area_subparte:
			porcentagem.append(float(pixelsbrancos[l+j])/float(area_subparte))
		cv.Copy(regiao_de_interesse,quadrante[l+j])
		cv.ResetImageROI(regiao_de_interesse)

    if porcentagem:
	vetor_de_caracteristicas = array ([porcentagem])
	code_word = vq(vetor_de_caracteristicas,code_book)
	if len(simbolos)==15:
		probabilidades = []
		sequencia_a_ser_avaliada = EmissionSequence(sigma,simbolos)
		probabilidades.append(HMM_passo_para_direita.viterbi(sequencia_a_ser_avaliada)[1])
		probabilidades.append(HMM_passo_para_esquerda.viterbi(sequencia_a_ser_avaliada)[1])
		probabilidades.append(HMM_levantar_braco_direito.viterbi(sequencia_a_ser_avaliada)[1])
		probabilidades.append(HMM_levantar_braco_esquerdo.viterbi(sequencia_a_ser_avaliada)[1])
		probabilidades.append(HMM_levantar_ambos_os_bracos.viterbi(sequencia_a_ser_avaliada)[1])
		simbolos=[]
	else:
		simbolos.append(code_word[0][0])

    print simbolos
    print probabilidades



    cv.ShowImage("Video",imagem)
    cv.ShowImage('Regiao de Interesse',regiao_de_interesse)
    cv.ShowImage("Mascara", mascara)
    #cv.ShowImage("Binario", cinza)

    cv.WaitKey( waitPerFrameInMillisec  )

