import cv

captura = cv.CaptureFromCAM(0)
cv.NamedWindow("Webcam", 1)

while True:
    imagem = cv.QueryFrame(captura)
    cv.ShowImage("Webcam", imagem)
    if cv.WaitKey(7) % 0x100 == 27:
        break

