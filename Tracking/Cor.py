import cv

def detectaCor(imagem):
    cv.Smooth(imagem,imagem,cv.CV_GAUSSIAN,3)
    cv.CvtColor(imagem, imagem, cv.CV_BGR2HSV)
    mascara = cv.CreateImage(cv.GetSize(imagem), 8, 1)
    cor_minima = (0, 50, 100)
    cor_maxima = (5, 255, 255)
    cv.InRangeS(imagem, cv.Scalar(*cor_minima), cv.Scalar(*cor_maxima), mascara)
    armazenamento = cv.CreateMemStorage(0)
    contornos = cv.FindContours (mascara, armazenamento, cv.CV_CHAIN_APPROX_NONE)
    for contorno in contornos:
        tamanho = abs(cv.ContourArea(contorno))
        convexo = cv.CheckContourConvexity(contorno)
        retangulo = cv.BoundingRect (contorno, 0)
        x = retangulo.x + retangulo.width*0.5
        y = retangulo.y + retangulo.height*0.5

        print(x,y)

    cv.CvtColor(imagem, imagem, cv.CV_HSV2BGR)
    cv.NamedWindow("Webcam", 1)
    cv.ShowImage("Webcam", imagem)
    #cv.NamedWindow("Mascara", 1)
    #cv.ShowImage("Mascara", mascara)



captura = cv.CaptureFromCAM(1)
while  True:

    imagem = cv.QueryFrame(captura)
    cv.Flip(imagem, None, 1)
    detectaCor(imagem)
    if cv.WaitKey(7) % 0x100 == 27:
        break

