from SimpleCV import *
from SimpleCV.Display import *
from time import sleep
k = Kinect()
dis = Display()
while 1:
	depth = k.getDepth()
	depth = depth.invert()
	depth = depth.erode()
	"""lines = depth.findLines(threshold=80, minlinelength=30, maxlinegap=10, cannyth1=50, cannyth2=100)
	if lines:
		lines.draw()
	corn = depth.findCorners(maxnum=1000, minquality=0.04, mindistance=1.0)
	if corn:
		corn.draw()
	img = k.getImage()"""
	blobs = depth.findBlobs(threshval=127, minsize=50, maxsize=0)
	if blobs:
		wid = blobs.width()
		leng = blobs.length()
		area = blobs.area()
		coords = blobs.coordinates()
		blobs.draw()
		print leng, area, coords
	depth.save(dis)
	sleep(0)
