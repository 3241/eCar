#! /usr/bin/python

import threading
from time import sleep
from select import select

# Exceptions 
class FinishFifoGet(Exception): pass
class InvalidData(StandardError): pass

def return_true(*args):
	return True

def fifo_get(fifo = "test", finish_case = None):
	if not finish_case:
		finish_case = return_true
	try:
		fifo_f = open(fifo,'r')
		while finish_case():
			line = False
			r,w,x = select([fifo_f],[],[], 0.2)
			if r:
				line=fifo_f.read()
				yield line.strip()
	finally:
		fifo_f.close()


def got_some_fifo_data(data):
	try:
		key, value =  data.split(":")
		key = key.strip()
		value = value.strip()
	except ValueError: 
		raise InvalidData("unpacking failed: (More or less than one colon were received)")
	print "Key: %s, Value: %s" % (key,value)

class FifoLink(threading.Thread):
	def __init__(self, filename, handler, startnow = True):
		super(FifoLink, self).__init__()
		self.filename = filename
		self.handler = handler
 		self.keeprunning = threading.Event()
 		self.keeprunning.clear()
 		if startnow:
			self.start()
		
	def stop(self):
		self.keeprunning.clear()
	
	def run(self):
		self.keeprunning.set()
		for line in fifo_get(self.filename, self.keeprunning.isSet):
			self.handler(line)

def test_handler(dat):
	print "From Fifo: %s" % dat

def tests():
	lnk = FifoLink("test_link", test_handler)
	try:
		while 1:
			print "Running main loop"
			sleep(5)
			
	except KeyboardInterrupt:
		lnk.stop()
		
			
if __name__ == "__main__":
	tests()