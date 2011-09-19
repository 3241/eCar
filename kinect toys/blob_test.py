from SimpleCV import *
from SimpleCV.Display import Display

d=Display()
k=Kinect()

while True:
	image=k.getDepth()
	blobs = image.findBlobs(200)
	try:
		for b in blobs:
			b.draw((255,0,0))
	except TypeError:
		pass
	image.save(d)