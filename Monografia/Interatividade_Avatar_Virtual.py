# -*- coding: utf-8 -*-
import cv
from numpy import array
from scipy.cluster.vq import vq
from os import system
from Code_Book import code_book
from Treino_HMM import *
from ghmm import *
from Avatar_Animado import *

#Configuracoes :
divisoes_para_vetor_de_caracteristicas = 6
tolerancia = 30
filtro_de_gauss = 3
filtro_de_dilatacao = 2
filtro_de_erosao = 2
resolucao_largura = 640
resolucao_altura = 480

fonte_do_texto = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 0.7, 0.7, 0, 2, 8)
video = cv.CaptureFromFile('videos/testar_todos.avi')
frames_total = int( cv.GetCaptureProperty( video, cv.CV_CAP_PROP_FRAME_COUNT ) )
fps = cv.GetCaptureProperty( video, cv.CV_CAP_PROP_FPS )
waitPerFrameInMillisec = int( 1/fps * 1000/1 )

cv.NamedWindow("Video", 1)
cv.NamedWindow("Mascara", 0)
cv.NamedWindow("Binario", 0)
cv.MoveWindow("Mascara",1200,0)
cv.MoveWindow("Video",730,480)
cv.MoveWindow("Binario",720,0)
#cv.NamedWindow("Regiao de Interesse", 1)
#cv.MoveWindow("Regiao de Interesse",650,0)

mascara = cv.CreateImage((resolucao_largura,resolucao_altura), 8, 3)
cinza = cv.CreateImage((resolucao_largura,resolucao_altura), 8, 1)
fundo = cv.LoadImage('videos/fundo.jpg')
cv.Smooth(fundo,fundo,cv.CV_GAUSSIAN,filtro_de_gauss)

nomeGesto = ''
simbolos = []
probabilidades = []

for f in xrange( frames_total ):
    #system('clear')

    imagem = cv.QueryFrame(video)
    cv.Smooth(imagem,imagem,cv.CV_GAUSSIAN,filtro_de_gauss)
    maiorArea = None
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


    if len(simbolos)==30:
	probabilidades = []
	sequencia_a_ser_avaliada = EmissionSequence(sigma,simbolos)

	probabilidade_de_passo_direita = HMM_passo_para_direita.viterbi(sequencia_a_ser_avaliada)
	if probabilidade_de_passo_direita[0][0] != -1:
		probabilidades.append(probabilidade_de_passo_direita[1])
	else:
		probabilidades.append(None)

	probabilidade_de_passo_esquerda = HMM_passo_para_esquerda.viterbi(sequencia_a_ser_avaliada)
	if probabilidade_de_passo_esquerda[0][0] != -1:
		probabilidades.append(probabilidade_de_passo_esquerda[1])
	else:
		probabilidades.append(None)

	probabilidade_de_braco_direito = HMM_levantar_braco_direito.viterbi(sequencia_a_ser_avaliada)
	if probabilidade_de_braco_direito[0][0] != -1:
		probabilidades.append(probabilidade_de_braco_direito[1])
	else:
		probabilidades.append(None)

	probabilidade_de_braco_esquerdo = HMM_levantar_braco_esquerdo.viterbi(sequencia_a_ser_avaliada)
	if probabilidade_de_braco_esquerdo[0][0] != -1:
		probabilidades.append(probabilidade_de_braco_esquerdo[1])
	else:
		probabilidades.append(None)

	probabilidade_de_ambos_bracos = HMM_levantar_ambos_os_bracos.viterbi(sequencia_a_ser_avaliada)
	if probabilidade_de_ambos_bracos[0][0] != -1:
		probabilidades.append(probabilidade_de_ambos_bracos[1])
	else:
		probabilidades.append(None)

	simbolos=[]
    else:
	if not all([ v == 0.0 for v in porcentagem ]) :
		vetor_de_caracteristicas = array ([porcentagem])
		code_word = vq(vetor_de_caracteristicas,code_book)
		simbolos.append(code_word[0][0])

    #print simbolos
    #print probabilidades
    if probabilidades:
	maiorProbabilidade = max(probabilidades)
	maiorProbabilidade_Index = probabilidades.index(maiorProbabilidade)

	if(maiorProbabilidade_Index == 0 and maiorProbabilidade == None):
		nomeGesto = ''
	if(maiorProbabilidade_Index == 0 and maiorProbabilidade != None):
		nomeGesto = 'Passo para Direita/Step Right'
		sequencia_de_animacoes.append(caminhar_direita)
	if maiorProbabilidade_Index == 1:
		nomeGesto = 'Passo para Esquerda/Step Left'
		sequencia_de_animacoes.append(caminhar_esquerda)
	if maiorProbabilidade_Index == 2:
		nomeGesto = 'Braco Direito Para Cima/Right Arm Up'
		sequencia_de_animacoes.append(levantar_braco_direito)
	if maiorProbabilidade_Index == 3:
		nomeGesto = 'Braco Esquerdo Para Cima/Left Arm Up'
		sequencia_de_animacoes.append(levantar_braco_esquerdo)
	if maiorProbabilidade_Index == 4:
		nomeGesto = 'Ambos os Bracos Para Cima/Both Arms Up'
		sequencia_de_animacoes.append(levantar_ambos_os_bracos)

	probabilidades = []

    cv.PutText(imagem, nomeGesto, (80,435) ,fonte_do_texto , cv.CV_RGB(255,255,255))

    cv.ShowImage("Video",imagem)
    cv.ShowImage("Mascara", mascara)
    cv.ShowImage("Binario", cinza)
    #cv.ShowImage('Regiao de Interesse',regiao_de_interesse)

    if sequencia_de_animacoes and estado_avatar==parado:
        estado_avatar = sequencia_de_animacoes.pop(0)
        frame_da_animacao=0

    tick_time = clock.tick(fps)
    pygame.display.set_caption("Ambiente Virtual. FPS: %.2f" % (clock.get_fps()))

    if estado_avatar==caminhar_direita:
        posicao_X_do_avatar = posicao_X_do_avatar + 5
    if estado_avatar==caminhar_esquerda:
        posicao_X_do_avatar = posicao_X_do_avatar - 5

    if (frame_da_animacao==28):
        frame_da_animacao=0
        estado_avatar = parado

    else:
        frame_da_animacao=frame_da_animacao+1

    screen.blit(fundo_ambiente_virtual,(0,0))
    screen.blit(estado_avatar[frame_da_animacao],(posicao_X_do_avatar,posicao_Y_do_avatar))
    pygame.display.update()

    cv.WaitKey( waitPerFrameInMillisec  )

