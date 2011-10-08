"""For what little difference it makes, the defacto python distribution used for this
        project (And particularly the test computer) is Python 2.7"""
"""To talk with the Motor Controller, will need PyUSB on your computer"""
import usb
""""SimpleCV is required for image recognition and camera control"""
import cv
"""Normal Modules to import"""
import math
import time


"""REMINDER TO EVERYONE PLEASE:
        Please use the metric system, we really don't want to
            crash the robot into Mars...
	Please disregard the apove statment

        Couple of baselines rules here:
            Angles are measured from the robot's straight ahead view. That means that
                something in the left side of the field of view would have a negative angle,
                while something to the right of the bot is positive. That means that we should
                never have an angle larger or smaller that +- 180 degrees. (Please use degrees
                instead of radians, makes things nicer...)
            Again, use the SI system, that means, if I want to measure distance,
                it's measured in meters, time is in seconds, and mass is in kg.
            Motor speeds are designated as seperate left and right motors in percentages of
                motor max speed. So If I want to go full speed, the variable should be 1.
                For going backwards, the speed will be negative percents.
"""    


class Map(object):
	def __init__(self, map_data):
		"""Parse `map_data`, and generate internal representation of map."""

	def position_for_glyph(self, glyph):
		"""Take a glyph string and return the map-position."""

class Route(object):
	""""""
	def __init__(self, route_data):
		"""Parse `map_data`, and generate internal representation of route."""

	def direction_for_position(self, map_position):
		pass

class Controller(object):
    """This is the brain of the robot. It decides how the robot responds to a given situation."""
    def __init__(self, interpreter=None, io=None):
        """Set controller's internal instances of interpreter and io to the arguments given."""
        if interpreter==None:
            interpreter = Interpreter()
        else:
            self.interpreter = interpreter
        if io==None:
                io = IO()   #need to add reasonable defaults for IO here.
        else:
            self.io = io
        interpreter.controller=self
        io.controller=self
        self.obstacles = []
        self.robot_width = 1
        self.left_speed = 0
        self.right_speed = 0
        self.total_speed = 0.5*(self.left_speed+self.right_speed)
            
    def received_obstacle(self, obstaclelist):
        #All we need is a list of all obstacles that the Kinect sees in one frame
        #This function will be called every single cycle, and will determine a new motor control structure every single cycle
        """Respond to obstacle by varying path."""
        """Receive object as a tuple (identifier, Left_magnitude, Left_angle,
                                        Right_magnitude, Right_angle)
            Assume flat surface between two angles (I know, I know)
            The ultimate hope is that image recognition can identify persistant
                obstacles between frames and report them thus, but not for now.
            (Note, I can write up an expected object movement module at some point
                if it is needed.)"""
        """CHOP CHOP I cut out the original reactive steering system in preference to a different one"""
        """New Reactive steering system!
                This system is will determine the 'gaps' between objects and then decide whether or not
                the robot can fit through them.
                ***THIS IS COMPLETELY EXPERIMENTAL, IT PROBABLY WORK***"""
        """     1. Sort all obstacles from left to right in view.
                2. Chop obstacles down so that we only look at everything 3 robot lengths in front of the robot.
                        (Note, this will maintain object postition and angles, but only for the area immediately
                                at the front of the robot up to the 3 length limit)"""
        
        
    def received_target(self, direction, certainty=1):
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


class IO(object):
	"""This class deals with input and output with the robot for communications over USB. This includes the microchip, the camera, and the kinect."""
	def __init__(self, devices):
		"""Takes file handles, or some way of referencing all of the the devices it will comunicate with. It will initialize connections to each of the devices and listen for data. Also sets the objects's interpreter field to the ones that is passed as an argument."""
	def received_data(self,source, data):
		"""Takes data from a given source and passes it to the appropriate method in the interpreter. (`received_ultrasonic`, `received_top_camera`, or `received_kinect`)"""
	def motor_speed(left=None, right=None):
		"""Sets the left and/or right speed. Only set speeds that are not None."""
	
