import cv 

video = cv.CaptureFromFile('levantar_bracos.avi')
#cv.SetCaptureProperty(video,cv.CV_CAP_PROP_FPS,15)
frames_total = int( cv.GetCaptureProperty( video, cv.CV_CAP_PROP_FRAME_COUNT ) )
fps = cv.GetCaptureProperty( video, cv.CV_CAP_PROP_FPS )
waitPerFrameInMillisec = int( 1/fps * 1000/1 )

cv.NamedWindow("Video", 1)


for f in xrange( frames_total ):
#while True :
	print cv.GetCaptureProperty( video, cv.CV_CAP_PROP_POS_MSEC)
	frame = cv.QueryFrame(video)
	cv.ShowImage("Video",frame)
	cv.WaitKey( waitPerFrameInMillisec  )
	#if cv.WaitKey(7) % 0x100 == 27:
		#break

print 'Numero de Frames = ', frames_total
print 'Frame Rate = ', fps, ' frames por segundo'

