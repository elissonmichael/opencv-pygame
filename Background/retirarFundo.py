import cv

captura = cv.CaptureFromCAM(1)
cv.NamedWindow("Fundo", 0)
cv.NamedWindow("Webcam", 0)
cv.NamedWindow("Mascara", 0)
cv.NamedWindow("Cinza", 0)
#cv.NamedWindow("Resultado", 0)

tolerancia = 50

mascara = cv.CreateImage((640,480), 8, 3)
cinza = cv.CreateImage((640,480), 8, 1)
resultado = cv.CreateImage((640,480), 8, 1)


while True:
    print ("Por Favor tire uma foto do fundo estatico do seu video.")
    print ("Aperte a tecla espaco.")
    if cv.WaitKey(0) % 0x100 == 32:
        fundo = cv.QueryFrame(captura)
        cv.Smooth(fundo,fundo,cv.CV_GAUSSIAN,3)
        cv.ShowImage("Fundo", fundo)
        print ("Tirou uma Foto !")
        break

while True:

    imagem = cv.QueryFrame(captura)

    cv.Smooth(imagem,imagem,cv.CV_GAUSSIAN,3)
    cv.ShowImage("Webcam", imagem)

    cv.AbsDiff(imagem,fundo,mascara)
    cv.CvtColor(mascara, cinza, cv.CV_BGR2GRAY)
    cv.Threshold(cinza,cinza,tolerancia,255,cv.CV_THRESH_BINARY)

   # cv.SetZero(resultado)
   # cv.And(imagem, imagem, resultado, cinza)

    cv.ShowImage("Cinza", cinza)
    cv.ShowImage("Mascara", mascara)
    #cv.ShowImage("Resultado",resultado)

    if cv.WaitKey(7) % 0x100 == 27:
        break

