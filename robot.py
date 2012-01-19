#! /usr/bin/python
from __future__ import division
import time
import os
import freenect
import pyroomba
import math
import pickle

class AI():
    def __init__(self):
        self.setup()
        
    def setup(self):
        self.minobjectwidth = 5 #Pixels
        self.distancethreshold = 100 #arbitrary units
        self.distanceuncertainty = 10
        self.floor = [] #Must fill this with measurements!
        self.correctdestinationthreshold = 10 #pixels
        self.correctheadingthreshold = 0.1 #Radians
        self.correctheading = False
        self.currentheading = 0
        self.newheading = 0
        self.stopped = False
        self.power = 100 #Standard (safe) speed
        self.offset = 0 #Radians
        self.fieldofview = 0.995 #radians (or 57 degrees)
        self.pixelsperrad = 640/self.fieldofview #I'm pretty sure
        self.turnradpersec = 0.66#This is an estimate, really ought to check (based on 1 rev/6 secs)
        #self.floor = pickle.load(open(os.path.expanduser('~/Dropbox/blankslate.sohl'),'rb')).transpose()
        #roomba = pyroomba.Roomba("/dev/tty.roomba")   #MAC ONLY
        self.roomba = pyroomba.Roomba("/dev/rfcomm1")    #Linux Only!
        self.roomba.start()
        self.roomba.safe()        
        print "Initialized Startup"
        self.mainloop()
    
    def determineDirection(self,heading):
        if self.currentheading>heading-self.correctheadingthreshold and self.currentheading<heading+self.correctheadingthreshold:
            self.correctheading = True
            return "Straight"
        elif self.currentheading-heading > 0:
            return "Left"
        elif self.currentheading-heading < 0:
            return "Right"
        else:
            print "ERROR, ERROR!" 
    def groupPillars(self,pillars):
        """Split pillar array into an array of pillar closest object distances
        i.e. Each grouping will display distance of closest object within pillar, or 
        'None' for no object"""
        #find closest point on each pillar
        pillardist = []
        #pillarcount = 0
        for pillar in pillars:
            closedist = 2047
            #floorpillar = self.floor[pillarcount]
            for pixel in range(0,len(pillar)):
                """Assumably, the pillar will be an array of distance measurements
                This can be compared to either an known array of floor recession measurements
                     or an algorithm (assumably exponential) to what it should be based on camera height
                (Note: measurement tolerences are likely to change, especially when camera bounce is properly
                     analyzed)"""
                if int(2047)-int(pillar[pixel])-self.distancethreshold > 0:
                    curdist = pillar[pixel]
                    if curdist<closedist:
                        closedist=curdist
            pillardist.append(closedist)
        return pillardist
            #pillarcount+=1
        #group pillars into 5-object groups. This can be changed as necessary
        #Takes average distance value
        #newgroup = []
        #for i in range(0,len(pillardist)):
            #if i%5==0 or i==len(pillardist)-1:
                #total = 0
                #nonecount = 0
                #for j in range(0,5):
                    #if pillardist[i]==None:
                        #total+=0
                        #nonecount+=1
                    #else:
                        #total+=pillardist[i]
                #if nonecount==5:
                    #average=None
                #else:
                    #average = total/(5-nonecount)
            #newgroup.append(average)
        #return newgroup
            
    def receivePillars(self,pillars):
        """Takes Pillar Array and determines appropriate heading"""
        """Analyze environment and choose a gap to go through"""
        groupedlist = self.groupPillars(pillars)
        print "Pillar Grouping Sequence Completed"
        #THIS IS TEMPORARY: scroll through pillar list and choose widest gap.
        #Yes, I realize that it may go in circles, but the short-term hope is that the Kinect's
        #     field of view will limit that.
        allgroups = []
        tempgroup = []
        tempgroup2 = []
        currentcount = 0
        for i in range(0,len(groupedlist)):
            #Slightly more complex now, the robot looks for the wider gap of further distance,
            #     based on the ration defined in 'self.distanceratio'.
           #For ease of programming, a 'block' is defined as a continuous series of pillars that
           #     are within an uncertainty defined as 'self.distanceuncertainty'. The program will
           #     step through the pillars until it discovers one at a different distance than the
           #     current, at which point it should continue on for 5 blocks, at which point it will
           #     either continue adding to the existing block, or create a new one, based on numbers. 
            if len(tempgroup)==0:
                tempgroup.append(i)
            elif groupedlist[i]<groupedlist[tempgroup[0]]+self.distanceuncertainty and groupedlist[i]>groupedlist[tempgroup[0]]-self.distanceuncertainty:
                tempgroup.append(i)
                currentcount = 0
                tempgroup2 = []
            else:
                tempgroup2.append(i)
                currentcount+=1
                if currentcount>=5:
                    allgroups.append(tempgroup)
                    tempgroup=tempgroup2
                    tempgroup2 = []
        allgroups.append(tempgroup)
        #Determine the distance/width Quotient
        allgroupsquotient = []
        widestgroup = 0
        farthestgroup = 0
        farthestscore = None
        highestscore = None
        for i in range(0,len(allgroups)):
            allgroupsquotient.append((groupedlist[allgroups[i][0]]/10)/(len(allgroups[i])))
            if groupedlist[allgroups[i][0]]<farthestscore or farthestscore==None:
                farthestgroup = i
                farthestscore = groupedlist[allgroups[i][0]]
            if abs(allgroupsquotient[i]-1)<highestscore or highestscore==None:
                highestscore = abs(allgroupsquotient[i]-1)
                widestgroup = i
        widestgroup = allgroups[widestgroup]
        #Determine pixel offset from center
        centerofimage = int(len(groupedlist)/2) #should be about 320 pixels
        targetblock = widestgroup[int(len(widestgroup)/2)]
        targetpixel = targetblock
        pixeloffset = targetpixel-centerofimage #i.e. 'right' is positive
        #This is a temporary fix for determining movement:
        radianoffset = pixeloffset/self.pixelsperrad
        self.correctheading=False
        self.newheading = radianoffset
        print "New Heading: "+str(self.newheading)

    def get_depth(self):
        temp = freenect.sync_get_depth()
        return temp[0]
    
    def get_depth_transposed(self):
        return self.get_depth().transpose()    

    def mainloop(self):
            while 1:
                """Check to determine if heading is correct"""
                f = open(os.path.expanduser('~/Dropbox/newdir'),'r')
                firstline = f.readline()
                if not firstline=="None\n":
                    if firstline=="Stop\n":
                        self.roomba.drive_direct(0,0)
                        self.correctheading=True
                        self.stopped = True
                    else:
                        self.newheading = math.radians(float(firstline))
                        self.correctheading = False
                        self.stopped=False
                        print "Determining New Direction"
                    f.close()
                    f1 = open(os.path.expanduser('~/Dropbox/newdir'),'w', 0)
                    f1.writelines(["None\n"])
                else:
                    f.close()
                if self.stopped==False:
                    while self.correctheading == False:
                        """If it is not correct, begin turning the bot"""
                        result = self.determineDirection(self.newheading)
                        if result=="Straight":
                            self.roomba.drive_direct(self.power,self.power)
                            self.correctheading = True
                            self.newheading = 0
                            print "Correct Heading acquired"
                        elif result=="Left":
                            self.roomba.drive_direct(self.power,-self.power)
                            time.sleep(0.01)
                            self.currentheading+=-self.turnradpersec*0.01
                        elif result=="Right":
                            self.roomba.drive_direct(-self.power,self.power)
                            time.sleep(0.01)
                            self.currentheading+=self.turnradpersec*0.01
                    self.currentheading = 0
                    print "Polling New Environment"
                    self.roomba.drive_direct(0,0)
                    time.sleep(0.1)
                    pillars = self.get_depth_transposed()
                    self.receivePillars(pillars)    
                    self.roomba.drive_direct(self.power,self.power)
                    if abs(self.newheading)<0.2:
                        time.sleep(4)
                    time.sleep(2)

App = AI()