class Controller(object):
	"""This is the brain of the robot. It decides how the robot responds to a given situation."""
	def __init__(self, interpreter=None, io=None):
		"""Set controller's internal instances of interpreter and io to the arguments given."""
		if interpreter==None:
			interpreter=Interpreter()
		if io==None:
			#need to add reasonable defaults for IO here.
			io=IO()
		interpreter.controller=self
		io.controller=self
		self.interpreter=interpreter
		self.io=io
		
	def received_obstacle(self, obstacle):
		"""Respond to obstacle by varying path."""
	def received_position(self, position):
		"""Report current position to server. Adjust course based on most accurate current position/orientation."""
	def ultrasonic_distance(self, distance):
		"""Perform the appropriate response for the distance returned."""

class Interpreter(object):
	"""Processes raw data from inputs. And sends the to the controller."""
	
	def received_ultrasonic(self,data):
		"""Processes ultrasonic data and sends it to the controller's `ultrasonic_distance` method."""
		
	def received_top_camera(self,data):
		"""Processes `data` and if it finds a glyph, determines the relative position of the bot to the glyph and calls the controller's `received_position` method. """
		
	def received_kinect(self,data):
		"""Processes the kinect data and looks for obstacles. For any obstacles it finds, it calls `received_obstacle` on the controller."""
        def Hunter_Is_Totally_Awsome(self):
                """This is just for me"""

class IO(object):
	"""This class deals with input and output with the robot for communications over USB. This includes the microchip, the camera, and the kinect."""
	def __init__(self, devices):
		"""Takes file handles, or some way of referencing all of the the devices it will comunicate with. It will initialize connections to each of the devices and listen for data. Also sets the objects's interpreter field to the ones that is passed as an argument."""
	def received_data(self,source, data):
		"""Takes data from a given source and passes it to the appropriate method in the interpreter. (`received_ultrasonic`, `received_top_camera`, or `received_kinect`)"""
	def motor_speed(left=None, right=None):
		"""Sets the left and/or right speed. Only set speeds that are not None."""
