import cv

video = cv.CaptureFromFile('levantar_bracos.avi')
frames_total = int( cv.GetCaptureProperty( video, cv.CV_CAP_PROP_FRAME_COUNT ) )

cv.NamedWindow("Video", 1)

class Filtros:
	def __init__(self):
		#self.imagem = imagem 
		frame = 0
		cv.CreateTrackbar("Frames", "Video", 0, frames_total-1, self.atualiza_frame)
		self.atualiza_frame(frame)

	def atualiza_frame(self,frame):
		cv.SetCaptureProperty(video,cv.CV_CAP_PROP_POS_FRAMES,frame)
		self.imagem = cv.QueryFrame(video)
		cv.ShowImage("Video",self.imagem)

if __name__ == "__main__":
	Filtros()
	cv.WaitKey(0) 
	print("Elisson Michael : [UENF] ")
