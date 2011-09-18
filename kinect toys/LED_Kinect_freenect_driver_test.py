#!/usr/bin/env python
import freenect
import time
import random
import signal

keep_running = True
last_time = 0

led_color=0;

def body(dev, ctx):
    global last_time
    global led_color
    if not keep_running:
        raise freenect.Kill
    if time.time() - last_time < 1:
        return
    last_time = time.time()
    freenect.set_led(dev, led_color%3+1)
    print led_color
    led_color+=1

def handler(signum, frame):
    """Sets up the kill handler, catches SIGINT"""
    global keep_running
    keep_running = False
print('Press Ctrl-C in terminal to stop')
print('The kinect LED should go solid green solid red solid orange, repeat. ')
signal.signal(signal.SIGINT, handler)
freenect.runloop(body=body)
