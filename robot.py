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

        Couple of baselines rules here:
            Angles are measured from the robot's straight ahead view. That means that
                something in the left side of the field of view would have a negative angle,
                while something to the right of the bot is positive. That means that we should
                never have an angle larger or smaller that +- 180 degrees. (Please use degrees
                instead of radians, makes things nicer...)
            Again, use the SI system, that means, if I want to measure distance,
                it's measured in meters, time is in seconds, and mass is in kg.
"""    


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
            
    def received_obstacle(self, obstacle):
        """Respond to obstacle by varying path."""
        """Receive object as a tuple (identifier, Left_magnitude, Left_angle,
                                        Right_magnitude, Right_angle)
            Assume flat surface between two angles (I know, I know)
            The ultimate hope is that image recognition can identify persistant
                obstacles between frames and report them with the same identifier here.
            (Note, I can write up an expected object movement module at some point
                if it is needed."""
        #This simply updates the total list of obstacles that we like keeping about
        recognized = False
        for obj in self.obstacles:
            if obstacle[0] == obj[0]:
                #If the obstacle is already known, just update it
                obj = obstacle
                recognized = True
        if recognized == False:
            #Otherwise, make a new one
            self.obstacles.append(obstacle)
        """WEEE! Reactive steering! This simply looks at how big the obstacle is
                and where it's at and steers away from it if it's in a collision course."""
        #Determine whether either point designated by the Tuple is within the straight-line
            #course of the robot
        left_x = obstacle[1]*math.sin(math.radians(obstacle[2]))
        right_x = obstacle[1]*math.sin(math.radians(obstacle[4]))
        #Figure out whether its to the left, right, or center and do something about it
        if (obstacle[2]>=0)and(obstacle[4]>=0):
            #Entire OBstacle is to the right of the robot center
            if obstacle[2]>(self.robot_width/2):
                #Obstacle is beyond the current collision path of the robot,
                #No action needed
                pass
            else:
                #Action required to steer left
                """Must fill in the appropriate motor control information here"""
                pass
        elif (obstacle[2]<0)and(obstacle[4]<0):
            #Entire Obstacle is to the left of the robot center
            if obstacle[4]<(-self.robot_width/2):
                #Obstacle is beyond the current collision path of the robot,
                #No action is needed
                pass
            else:
                #Action required to steer right
                """Must fill in the appropriate motor control information here"""
                pass
        else:
            #obstacle is centered on the robot
            """For the moment this is simply going to attempt to steer towards the
                side of the obstacle that is lesser, until one of the other contingencies
                sets in. If the obstacle is absolutely straight on, it will go the right.
                    (NOTE: This is temporary, this bit absolutely requires to have multi-
                        obstacle handling to determine the best accepted course between
                        all obstacles in the area when confronted with this situation."""
            if abs(obstacle[2])<abs(obstacle[4]):
                #steer to the left
                pass
            else:
                #steer to the right
                pass
                
        
        
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


class IO(object):
	"""This class deals with input and output with the robot for communications over USB. This includes the microchip, the camera, and the kinect."""
	def __init__(self, devices):
		"""Takes file handles, or some way of referencing all of the the devices it will comunicate with. It will initialize connections to each of the devices and listen for data. Also sets the objects's interpreter field to the ones that is passed as an argument."""
	def received_data(self,source, data):
		"""Takes data from a given source and passes it to the appropriate method in the interpreter. (`received_ultrasonic`, `received_top_camera`, or `received_kinect`)"""
	def motor_speed(left=None, right=None):
		"""Sets the left and/or right speed. Only set speeds that are not None."""
