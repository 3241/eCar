from SimpleCV import *
import time

k=Kinect()
js=JpegStreamer()

while 1:
    k.getDepth().save(js)
    time.sleep(0.1)

