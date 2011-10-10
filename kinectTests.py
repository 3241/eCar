from SimpleCV import *
from SimpleCV.Display import *
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
		blob_array = depth_image.findBlobs(threshval=127, minsize=50, maxsize=0)
		return(blob_array)
	def get_theadaus(self, blob_array):
		"""Here it will find the angle theadaus for each blob and return theadau_array"""
		pixel_widths = blobs.width()
		pixel_widths = divide(pixel_widths, img_width)
		return(multiply(pixel_width, kinect_max_angle))
	def get_outside_points(self, blob_array):
		"""Here it will find the farthest left and the farthest right point for all blobs and return
			outside_coord_array"""
		pass
	def get_width(self, outside_coord_array, theadau_array):
		"""Here it will calculate the actuall width for each of the objects it will be completely independant 				of inch or meters for we will do that earlier in the code, it will return width_array"""
		"""width = right_point(squared) + left_point(squared) - 2(right_point*left_point*cos(theadau))"""
		blob_width_array = []
		for i in range(len(theadau_array):
			blob_width_array.append(pow(outside_coord_array[i][0],2)+pow(outside_coord_array[i][1],2)
				- (2*outside_coord_array[i][0]*outside_coord_array[i][1]*cos(theadau_array[i]))
		return(blob_width_array)

if __name__ == "__Main__":
	inter = kinect_interpreter()
	while 1:
		depth = k.getDepth()
		"""converts the image into inches instead of mm"""
		depth = multiply(depth, inch_conver)
		"""Or we can use this to convert it into cm, or into m by changing 10 to 100"""
		#depth = divide(depth, 10)
		"""We will talk more about it"""
		"""inverts the image, since blob detect looks for lowest level pixels"""
		depth = depth.invert()
		"""Makes blobs easier to detect"""
		depth = depth.erode()
		blob_array = inter.blob_detect(depth)
		theadau_array = inter.get_theadaus(blob_array)
		outside_coord_array = inter.get_outside_points(blob_array)
		blob_width_array = inter.get_width
		print blob_width_array




