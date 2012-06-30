# -*- coding: utf-8 -*-
import cv
from numpy import array
from scipy.cluster.vq import vq
from os import system
from Code_Book import code_book
from Treino_HMM import *
from ghmm import *

#Configuracoes :
divisoes_para_vetor_de_caracteristicas = 6
filtro_de_gauss = 3
filtro_de_dilatacao = 2
filtro_de_erosao = 2
resolucao_largura = 640
resolucao_altura = 480

video = cv.CaptureFromFile('videos/braco_direito_4.avi')
frames_total = int( cv.GetCaptureProperty( video, cv.CV_CAP_PROP_FRAME_COUNT ) )

#cv.NamedWindow("Video", 0)
cv.NamedWindow("Mascara", 1)
#cv.NamedWindow("Binario", 1)
#cv.MoveWindow("Video",1000,510)
cv.MoveWindow("Mascara",0,0)
#cv.MoveWindow("Binario",650,0)
#cv.NamedWindow("Regiao de Interesse", 1)
#cv.MoveWindow("Regiao de Interesse",650,0)

mascara = cv.CreateImage((resolucao_largura,resolucao_altura), 8, 3)
cinza = cv.CreateImage((resolucao_largura,resolucao_altura), 8, 1)
fundo = cv.LoadImage('videos/fundo.jpg')
cv.Smooth(fundo,fundo,cv.CV_GAUSSIAN,filtro_de_gauss)

class Filtros:
        def __init__(self):
                frame = 0
                self.tolerancia = 30
                cv.CreateTrackbar("Frames", "Mascara", frame, frames_total-1, self.atualiza_frame)
                cv.CreateTrackbar("Tolerancia", "Mascara", self.tolerancia, 255, self.atualiza_tolerancia)
                self.atualiza_frame(frame)

        def processa(self):
                system("clear")
                maiorArea = None
                listaContornos = []
                listaVertices = []
                quadrante = []
                pixelsbrancos = []
                porcentagem = []

                cv.AbsDiff(self.imagem,fundo,mascara)
                cv.CvtColor(mascara, cinza, cv.CV_BGR2GRAY)
                cv.Threshold(cinza,cinza, self.tolerancia,255,cv.CV_THRESH_BINARY)

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


		global simbolos,probabilidades

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

                      simbolos = []
                else:
                      if not all([ v == 0.0 for v in porcentagem ]) :
	                      vetor_de_caracteristicas = array ([porcentagem])
	                      code_word = vq(vetor_de_caracteristicas,code_book)
	                      simbolos.append(code_word[0][0])

                print simbolos
                print probabilidades
                if probabilidades:
			maiorProbabilidade = max(probabilidades)
			maiorProbabilidade_Index = probabilidades.index(maiorProbabilidade)
			print maiorProbabilidade_Index
			if (maiorProbabilidade_Index == 0 and maiorProbabilidade!= None): print 'Passo para Direita        / Step Right'
			if maiorProbabilidade_Index == 1: print 'Passo para Esquerda       / Step Left'
			if maiorProbabilidade_Index == 2: print 'Braço Direito Para Cima   / Right Arm Up'
			if maiorProbabilidade_Index == 3: print 'Braço Esquerdo Para Cima  / Left Arm Up'
			if maiorProbabilidade_Index == 4: print 'Ambos os Braços Para Cima / Both Arms Up'

                self.mostrar()

        def atualiza_tolerancia(self,tolerancia):
                self.tolerancia = tolerancia
                self.processa()

        def atualiza_frame(self,frame):
                cv.SetCaptureProperty(video,cv.CV_CAP_PROP_POS_FRAMES,frame)
                self.imagem = cv.QueryFrame(video)
                cv.Smooth(self.imagem,self.imagem,cv.CV_GAUSSIAN,filtro_de_gauss)
                self.processa()

        def mostrar(self):
                #cv.ShowImage("Video",self.imagem)
                #cv.ShowImage('Regiao de Interesse',regiao_de_interesse)
                cv.ShowImage("Mascara", mascara)
                #cv.ShowImage("Binario", cinza)

if __name__ == "__main__":
	simbolos = []
	probabilidades = []
        Filtros()
        while True:
                tecla_apertada = cv.WaitKey(7) % 0x100
                if tecla_apertada == 27:
                        break
        print("Elisson Michael : [UENF] ")

