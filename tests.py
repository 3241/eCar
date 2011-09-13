"""This will be the main testing file."""

import robot

controller=robot.Controller()
controller.interpreter=robot.Interpreter()
controller.io=robot.IO("References to the cameras and chip")

#this should imply that if:
io=controller.io
interpreter=controller.interpreter
#then
print io.controller==controller
print interpreter.controller==controller
#evaluate to True.