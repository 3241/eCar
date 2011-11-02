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
	    self.currentheading = Bot.getHeading()
	def determineDirection(self,heading):
            if self.currentheading in range(-self.correctheadingthreshold,self.correctheadingthreshold):
                self.correctheading = True
                return "Straight"
            elif heading < 0:
                return "Left"
            elif heading > 0:
                return "Right"
        def groupPillars(self,pillars):
            """Split pillar array into array of pillar (distance,width) tuples"""
            #group pillars into 5 object groups
            groups = []
            newgroup = []
            for i in range(0,len(pillars)):
                if i%5==0 or i==len(pillars)-1:
                    groups.append(newgroup)
                    newgroup = []
                newgroup.append(pillars[i])
        def receivePillars(self,pillars):
            """Takes Pillar Array and determines appropriate heading"""
            """Check to determine if heading is correct"""
            while self.correctheading == False:
                """If it is not correct, begin turning the bot"""
                heading = bot.getHeading()
                result = determineDirection(heading)
                if result=="Straight":
                    bot.goForward()
                elif result=="Left":
                    bot.goLeft()
                elif result=="Right":
                    bot.goRight()
            """Analyze environment and choose a gap to go through"""
            groupPillars(pillars)
                    

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
