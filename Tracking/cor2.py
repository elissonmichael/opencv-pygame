import cv

def detectaCor(imagem):
    cv.Smooth(imagem,imagem,cv.CV_GAUSSIAN,3)
    cv.CvtColor(imagem, imagem, cv.CV_BGR2HSV)
    mascara = cv.CreateImage(cv.GetSize(imagem), 8, 1)
    cor_minima = (0, 50, 100)
    cor_maxima = (5, 255, 255)
    cv.InRangeS(imagem, cv.Scalar(*cor_minima), cv.Scalar(*cor_maxima), mascara)

    moments = cv.Moments(mascara, 0)
    area = cv.GetCentralMoment(moments, 0, 0)

    if(area > 10000):
        x = (cv.GetSpatialMoment(moments, 1, 0)/area)/5
        y = (cv.GetSpatialMoment(moments, 0, 1)/area)/5

        #print 'x: ' + str(x) + ' y: ' + str(y) #+ ' area: ' + str(area)
        overlay = cv.CreateImage(cv.GetSize(imagem), 8, 3)
        cv.Add(imagem, overlay, imagem)
        cv.Merge(mascara, None, None, None, imagem)

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

