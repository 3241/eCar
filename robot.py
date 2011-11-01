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
    pass
