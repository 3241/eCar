class Interpreter:
	"""Processes raw data from inputs. And sends the to the controller."""
	
	def received_ultrasonic(self,data):
		"""Processes ultrasonic data and sends it to the controller's `ultrasonic_distance` method."""
		
	def received_top_camera(self,data):
		"""Processes `data` and if it finds a glyph, determines the relative position of the bot to the glyph and calls the controller's `received_position` method. """
		
	def received_kinect(self,data):
		"""Processes the kinect data and looks for obstacles. For any obstacles it finds, it calls `received_obstacle` on the controller."""