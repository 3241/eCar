#! /bin/bash

class BotModule(object):
    def __init__(self, bot):
        self.bot = bot
        self.setup()
	
	def setup(self):
		pass
		
class IO(BotModule):
	def setup(self):
		pass

class Glyph(BotModule):
	def setup(self):
		pass

class KinectProcessing(BotModule):
	def setup(self):
		pass

class AI(BotModule):
	def setup(self):
		pass

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