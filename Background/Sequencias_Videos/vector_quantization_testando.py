import cv
from numpy import array
from scipy.cluster.vq import vq
from os import system

#Configuracoes :
filtro_de_gauss = 3
filtro_de_dilatacao = 4
filtro_de_erosao = 2
resolucao_largura = 640
resolucao_altura = 480


# Vector Quantization
code_book = array([                                                   \
		  [0.43548387096774194, 0.78893214682981094, 0.60984427141268072, 0.87569521690767516, 1.0, 0.79977753058954393, 0.71523915461624021, 0.92296996662958841, 0.35400444938820913],       \
		  [0.61015243025596777, 0.79824561403508776, 0.4069600230083405, 0.45197008915731951, 0.80069025021570317, 0.23295944779982744, 0.0, 0.38467069312625829, 0.47814207650273222],  \
		  [0.69217988480283565, 0.88003987594151534, 0.4098360655737705, 0.13458130261408949, 0.35832964111652638, 0.40451927337173238, 0.0, 0.0, 0.25155073105892778]                   \
		  [0.43489254  0.7471555   0.60714286  0.89475348  1.          0.92414665
  0.41845765  0.82901391  0.41213654]                                 \
  		  [ 0.          0.2453869   0.47678571  0.20639881  0.709375    0.51041667
  0.690625    0.77425595  0.40684524]                                 \
  		  [ 0.          0.0152381   0.3325      0.00892857  0.43607143  0.45666667
  0.71107143  0.81428571  0.46452381]                                 \
  		  [ 0.31616983  0.90840108  0.2435411   0.90153568  0.99891599  0.57289973
  0.42836495  0.9398374   0.42113821]                                 \
		  ])



video = cv.CaptureFromFile('andar_esquerda.avi')
frames_total = int( cv.GetCaptureProperty( video, cv.CV_CAP_PROP_FRAME_COUNT ) )

cv.NamedWindow("Video", 1)
cv.NamedWindow("Mascara", 1)
cv.NamedWindow("Binario", 1)
cv.NamedWindow("Regiao de Interesse", 1)
cv.MoveWindow("Regiao de Interesse",650,20)
cv.MoveWindow("Mascara",650,510)
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
			cv.Rectangle(mascara, ponto1, ponto2, cv.CV_RGB(255,255,255), 2)
			cv.Line(mascara,(ponto1[0]+largura/3,ponto1[1]),(ponto1[0]+largura/3,ponto2[1]), cv.CV_RGB(255,255,255), 1)
			cv.Line(mascara,(ponto1[0]+largura/3+largura/3,ponto1[1]),(ponto1[0]+largura/3+largura/3 ,ponto2[1]), cv.CV_RGB(255,255,255), 1)
			cv.Line(mascara,(ponto1[0],ponto1[1]+altura/3),(ponto2[0],ponto1[1]+altura/3), cv.CV_RGB(255,255,255), 1)
			cv.Line(mascara,(ponto1[0],ponto1[1]+altura/3+altura/3),(ponto2[0],ponto1[1]+altura/3+altura/3), cv.CV_RGB(255,255,255), 1)

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
		system("clear")
		vetor_de_caracteristicas = array ([porcentagem])
		resultado = vq(vetor_de_caracteristicas,code_book)
		print 'Vetor de features : '
		print vetor_de_caracteristicas[0]
		print 'Indice do codeword : '

		if resultado[0]==0: print 'Virado para Direita -> '
		if resultado[0]==1: print 'Passo Direita 1 -> '
		if resultado[0]==2: print 'Passo Direita 2 -> '
		if resultado[0]==3: print '<- Virado para Esquerda '
		if resultado[0]==4: print '<- Passo Esquerda 1 '
		if resultado[0]==5: print '<- Passo Esquerda 2 '
		if resultado[0]==6: print ' - Parado de Frente - '

		print 'Distorcao : '
		print resultado[1]
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
		cv.ShowImage('Regiao de Interesse',regiao_de_interesse)
		cv.ShowImage("Mascara", mascara)
		cv.ShowImage("Binario", cinza)

if __name__ == "__main__":
	Filtros()
	cv.WaitKey(0)
	print("Elisson Michael : [UENF] ")

