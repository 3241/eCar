import cv
import time

window = cv.NamedWindow("camera", 1)
capture = cv.CreateCameraCapture(0)
width = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH)) 
height = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))


 
while 1:
    img = cv.QueryFrame(capture)
    cv.ShowImage("camera", img)
    k = cv.WaitKey(1)
    if(k == 102):
        cv.destroyWindow("camera")
        break
    

