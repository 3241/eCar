class IO:
	"""This class deals with input and output with the robot for communications over USB. This includes the microchip, the camera, and the kinect."""
	def __init__(self, interpreter, devices):
		"""Takes file handles, or some way of referencing all of the the devices it will comunicate with. It will initialize connections to each of the devices and listen for data. Also sets the objects's interpreter field to the ones that is passed as an argument."""
	def received_data(self,source, data):
		"""Takes data from a given source and passes it to the appropriate method in the interpreter. (`received_ultrasonic`, `received_top_camera`, or `received_kinect`)"""
	def motor_speed(left=None, right=None):
		"""Sets the left and/or right speed. Only set speeds that are not None."""