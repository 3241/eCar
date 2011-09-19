from SimpleCV import *
import time

k=Kinect()
js=JpegStreamer()

shape_x_size=10
shape_y_size=10

screen_size=1440, 900

red=(255.0, 0.0, 0.0)
green=(0.0, 255.0, 0.0)

import pymouse
m=pymouse.PyMouse()

while 1:
	dm=k.getDepthMatrix()
	amin=dm.argmin()
	shapex=dm.shape[0]
	shapey=dm.shape[1]
	x,y = amin%shapey,amin/shapey
	dep=k.getDepth()
	color = green if dm.ravel()[amin]<450 else red
	
	m.move(screen_size[0]-x*screen_size[0]/shapex,y*screen_size[1]/shapey)
	
	if x < shape_x_size:
		x = shape_x_size
	elif x > (shapex - shape_x_size):
		x = shapex - shape_x_size
	if y < shape_y_size:
		y = shape_y_size
	elif y > (shapey - shape_y_size):
		y = shapey - shape_y_size
		
	dep[(x-shape_x_size):x+shape_x_size , y-shape_y_size:y+shape_y_size]=color
	dep.save(js)
	time.sleep(0.1)



