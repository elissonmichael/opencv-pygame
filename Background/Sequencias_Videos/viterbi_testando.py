import cv
from numpy import array
from scipy.cluster.vq import vq
from os import system
from ghmm import *
from Vector_Quantization import code_book
from HMMs import HMM_passo_para_direita,sigma

#Configuracoes :
divisoes_para_vetor_de_caracteristicas = 5
filtro_de_gauss = 3
filtro_de_dilatacao = 4
filtro_de_erosao = 2
resolucao_largura = 640
resolucao_altura = 480

video = cv.CaptureFromFile('andar_direita.avi')
frames_total = int( cv.GetCaptureProperty( video, cv.CV_CAP_PROP_FRAME_COUNT ) )

cv.NamedWindow("Video", 1)
#cv.NamedWindow("Mascara", 1)
cv.NamedWindow("Binario", 1)
#cv.NamedWindow("Regiao de Interesse", 1)
#cv.MoveWindow("Regiao de Interesse",650,20)
#cv.MoveWindow("Mascara",650,510)
cv.MoveWindow("Binario",1000,510)

mascara = cv.CreateImage((resolucao_largura,resolucao_altura), 8, 3)
cinza = cv.CreateImage((resolucao_largura,resolucao_altura), 8, 1)
fundo = cv.LoadImage('fundo.jpg')
cv.Smooth(fundo,fundo,cv.CV_GAUSSIAN,filtro_de_gauss)

class Filtros:
	def __init__(self):
		frame = 211
		self.tolerancia = 35
		cv.CreateTrackbar("Frames", "Video", frame, frames_total-1, self.atualiza_frame)
		cv.CreateTrackbar("Tolerancia", "Video", self.tolerancia, 255, self.atualiza_tolerancia)
		self.atualiza_frame(frame)

	def processa(self):
		maiorArea = 0
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
			cv.Rectangle(self.imagem, ponto1, ponto2, cv.CV_RGB(255,255,255), 2)
			#cv.Line(mascara,(ponto1[0]+largura/3,ponto1[1]),(ponto1[0]+largura/3,ponto2[1]), cv.CV_RGB(255,255,255), 1)
			#cv.Line(mascara,(ponto1[0]+largura/3+largura/3,ponto1[1]),(ponto1[0]+largura/3+largura/3 ,ponto2[1]), cv.CV_RGB(255,255,255), 1)
			#cv.Line(mascara,(ponto1[0],ponto1[1]+altura/3),(ponto2[0],ponto1[1]+altura/3), cv.CV_RGB(255,255,255), 1)
			#cv.Line(mascara,(ponto1[0],ponto1[1]+altura/3+altura/3),(ponto2[0],ponto1[1]+altura/3+altura/3), cv.CV_RGB(255,255,255), 1)

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
				porcentagem.append(float(pixelsbrancos[l+j])/float(area_subparte))
				cv.Copy(regiao_de_interesse,quadrante[l+j])
				cv.ResetImageROI(regiao_de_interesse)
		system("clear")
		vetor_de_caracteristicas = array ([porcentagem])
		resultado = vq(vetor_de_caracteristicas,code_book)
		#print 'Vetor de features : '
		#print porcentagem
		sequencia_a_ser_avaliada = EmissionSequence(sigma,[resultado[0][0]])
		print sequencia_a_ser_avaliada
		viterbi = HMM_passo_para_direita.viterbi(sequencia_a_ser_avaliada)

		print viterbi

		self.mostrar()

	def atualiza_tolerancia(self,tolerancia):
		self.tolerancia = tolerancia
		self.processa()

	def atualiza_frame(self,frame):
		cv.SetCaptureProperty(video,cv.CV_CAP_PROP_POS_FRAMES,frame)
		self.imagem = cv.QueryFrame(video)
		#cv.SaveImage('fundo2.jpg',self.imagem)
		cv.Smooth(self.imagem,self.imagem,cv.CV_GAUSSIAN,filtro_de_gauss)
		self.processa()

	def mostrar(self):
		cv.ShowImage("Video",self.imagem)
		#cv.ShowImage('Regiao de Interesse',regiao_de_interesse)
		#cv.ShowImage("Mascara", mascara)
		cv.ShowImage("Binario", cinza)

if __name__ == "__main__":
	Filtros()
	cv.WaitKey(0)
	print("Elisson Michael : [UENF] ")

