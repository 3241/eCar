#! /usr/bin/python
import fifolink

class BotModule(object):
    def __init__(self, bot):
        self.bot = bot
        self.setup()
	
	def setup(self):
		pass
		
class IO(BotModule):
	def setup(self):
		self.fifo = fifolink.FifoLink("top_camera.fifo", self.receive_top_cam_data)
	
	def receive_top_cam_data(self, message):
		print "Recieved: %s, from the top camera." % message

class Glyph(BotModule):
	def setup(self):
		pass

class KinectProcessing(BotModule):
	def setup(self):
		pass

class AI(BotModule):
	def setup(self):
	    self.minobjectwidth = 5 #Pixels
	    self.correctdestinationthreshold = 10 #pixels
	    self.correctheadingthreshold = 0.087 #Radians
	    self.correctheading = False
	    self.currentheading = "Unknown"
	    self.estimatedheading = "Unknown"
	def GlyphMove(self,moveto,knownat):
            self.currentheading = knownat
            self.estimatedheading = knownat
            result = self.determineDirection(moveto,knownat)
            if result == "Left":
                self.bot.startLeft()
            elif result == "Right":
                self.bot.startRight()
            elif result == "Straight":
                self.bot.startForward()
	def determineDirection(self,movetoheading,currentheading):
            if self.currentheading in range(movetoheading-self.correctheadingthreshold,movetoheading+self.correctheadingthreshold):
                self.correctheading = True
                return "Straight"
            elif self.currentheading > movetoheading:
                return "Left"
            elif self.currentheading < movetoheading:
                return "Right"
        def receivePillars(self.pillars):
            """Takes Pillar Array and determines appropriate heading"""
            

class Bot(object):
    def __init__(self, botmodules = (AI, KinectProcessing, Glyph, IO)):
		self.setup_botmodules(botmodules)
	
	def setup_botmodules(self, botmodules):
		"""Configure the set `self.modules` as instances of the passed `botmodules` argument."""
		self.modules = set()
		for module in botmodules:
			try:
				self.modules.add(module(bot = self))
			except TypeError:
				raise TypeError("passed module: %s, is not a BotModule instance." % module)
