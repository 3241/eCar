#!/usr/bin/env python
import freenect
import time
import random
import signal

keep_running = True
last_time = 0


def body(dev, ctx):
    if not keep_running:
        raise freenect.Kill
    freenect.set_tilt_degs(dev, int(raw_input("Servo position? "))%31)


def handler(signum, frame):
    """Sets up the kill handler, catches SIGINT"""
    global keep_running
    keep_running = False
print('Press Ctrl-C in terminal to stop')
signal.signal(signal.SIGINT, handler)
freenect.runloop(body=body)