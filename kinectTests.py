from SimpleCV import *
from SimpleCV.Display import *
from numpy import *
from time import sleep
k = Kinect()
dis = Display()
"""The number required to convert mm to inches"""
inch_conver = 0.0393700787
"""The horizontal image resolution"""
img_width = 540
"""The maxiumum angle that the kinect can view"""
kinect_max_angle = 69
	
class kinect_interpreter(object):
	"""Outline for how class will work"""
	def blob_detect(self, depth_image):
		"""This will find all the blobs and return them in an array"""
		blob_array = depth_image.findBlobs(threshval=12, minsize=10, maxsize=0)
		return(blob_array)
	def get_theadaus(self, blob_array):
		"""Here it will find the angle theadaus for each blob and return theadau_array"""
		pixel_widths = blob_array.width()
		pixel_widths = divide(float(pixel_widths), float(img_width))
		return(multiply(pixel_widths, kinect_max_angle))
	def get_outside_points(self, blob_array):
		"""Here it will find the farthest left and the farthest right point for all blobs and return
			outside_coord_array"""
		pass
	def get_width(self, outside_coord_array, theadau_array):
		"""Here it will calculate the actuall width for each of the objects it will be completely independant 				of inch or meters for we will do that earlier in the code, it will return width_array"""
		"""width = right_point(squared) + left_point(squared) - 2(right_point*left_point*cos(theadau))"""
		blob_width_array = []
		for i in range(len(theadau_array)):
			blob_width_array.append(pow(outside_coord_array[i][0],2)+pow(outside_coord_array[i][1],2)
				- (2*outside_coord_array[i][0]*outside_coord_array[i][1]*cos(theadau_array[i])))
		return(blob_width_array)
	def run(self, depth):
		"""inverts the image, since blob detect looks for lowest level pixels"""
		depth = depth.invert()
		"""use this to convert it into cm, or into m by changing 10 to 100"""
		depth = divide(depth, 10)
		"""Makes blobs easier to detect"""
		depth = depth.erode()
		blob_array = self.blob_detect(depth)
		if blob_array:
			theadau_array = self.get_theadaus(blob_array)
			print theadau_array
			"""
			Untill i fill in outside coord array, i will get rid of this code
			outside_coord_array = self.get_outside_points(blob_array)
			blob_width_array = self.get_width(outside_coord_array, theadau_array)
			return blob_width_array	
			"""	
		return blob_array
if __name__ == "__main__":
	inter = kinect_interpreter()
	while 1:
		depth = k.getDepth()
		blobs = inter.run(depth)
		if blobs:
			blobs.draw()
		depth.save(dis)
		



