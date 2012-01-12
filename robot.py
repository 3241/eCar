#! /usr/bin/python
import time
import os
import freenect
import pyroomba

class AI():
    def setup(self):
        self.minobjectwidth = 5 #Pixels
        self.distancethreshold = 0.10 #m
        self.floor = [] #Must fill this with measurements!
        self.correctdestinationthreshold = 10 #pixels
        self.correctheadingthreshold = 0.087 #Radians
        self.correctheading = False
        self.currentheading = 0
        self.newheading = 0
        self.power = 100 #Standard (safe) speed
        self.offset = 0 #Radians
        self.fieldofview = 0.995 #radians (or 57 degrees)
        self.pixelsperrad = 640/self.fieldofview #I'm pretty sure
        self.turnradpersec = 1.05#This is an estimate, really ought to check (based on 1 rev/6 secs)
        self.floor = self.get_depth_transposed()
        self.mainloop()
    def mainloop(self):
        while 1:
            """Check to determine if heading is correct"""
            f = file(os.path.expanduser('~/Dropbox/newdir.txt'),'r')
            firstline = f.readline()
            if not firstline=="None":
                if firstline=="Stop":
                    roomba.drive_direct(0,0)
                else:
                    self.newheading = float(firstline)
                f.close()
                f1 = file(os.path.expanduser('~/Dropbox/newdir.txt'),'w')
                f1.writelines("None")
            else:
                f.close()
            while self.correctheading == False:
                """If it is not correct, begin turning the bot"""
                result = determineDirection(heading)
                if result=="Straight":
                    roomba.drive_direct(self.power,self.power)
                    self.correctheading = True
                    self.newheading = 0
                elif result=="Left":
                    roomba.drive_direct(self.power,-self.power)
                    time.sleep(0.2)
                    self.currentheading+=-self.turnradpersec*0.2
                elif result=="Right":
                    roomba.drive_direct(-self.power,self.power)
                    time.sleep(0.2)
                    self.currentheading+=self.turnradpersec*0.2
            pillars = self.get_depth_transposed()
            self.receivePillars(pillars)
    def determineDirection(self,heading):
        if self.currentheading in range(-self.correctheadingthreshold,self.correctheadingthreshold):
            self.correctheading = True
            return "Straight"
        elif heading < 0:
            return "Left"
        elif heading > 0:
            return "Right"
    def groupPillars(self,pillars):
        """Split pillar array into an array of pillar closest object distances
        i.e. Each grouping will display distance of closest object within pillar, or 
        'None' for no object"""
        #find closest point on each pillar
        pillardist = []
        for pillar in pillars:
            closedist = None
            for pixel in range(0,len(pillar)):
                """Assumably, the pillar will be an array of distance measurements
                This can be compared to either an known array of floor recession measurements
                     or an algorithm (assumably exponential) to what it should be based on camera height
                (Note: measurement tolerences are likely to change, especially when camera bounce is properly
                     analyzed)"""
                if pillar[pixel]<self.floor[pixel]-self.distancethreshold:
                    curdist = pillar[pixel]
                    if curdist<closedist:
                        closedist=curdist
            pillardist.append(closedist)
        #group pillars into 5-object groups. This can be changed as necessary
        #Takes average distance value
        newgroup = []
        for i in range(0,len(pillardist)):
            if i%5==0 or i==len(pillardist)-1:
                total = 0
                for j in range(0,5):
                    total+=newgroup[i]
                average = total/len(newgroup)
            newgroup.append(average)
        return newgroup
            
    def receivePillars(self,pillars):
        """Takes Pillar Array and determines appropriate heading"""
        """Analyze environment and choose a gap to go through"""
        groupedlist = groupPillars(pillars)
        #THIS IS TEMPORARY: scroll through pillar list and choose widest gap.
        #Yes, I realize that it may go in circles, but the short-term hope is that the Kinect's
        #     field of view will limit that.
        widestgroup = []
        tempgroup = []
        for i in range(0,len(groupedlist)):
            #For the moment, it will only look for 'None'
            if groupedlist[i]==None:
                tempgroup.append(i)
            else:
                if len(tempgroup)>len(widestgroup):
                    #Left-side preference, will fix
                    widestgroup=tempgroup
                    tempgroup = []
                else:
                    tempgroup = []
        #Determine pixel offset from center
        centerofimage = int(len(groupedlist)*5/2) #should be about 320 pixels
        targetblock = widestgroup[int(len(widestgroup)/2)]
        targetpixel = targetblock*5
        pixeloffset = targetpixel-centerofimage #i.e. 'right' is positive
        #This is a temporary fix for determining movement:
        if pixeloffset>0 and pixeloffset>self.correctheadingthreshold:
            roomba.drive_direct(-self.power,self.power)
        elif pixeloffset<0 and pixeloffset>self.correctheadingthreshold:
            roomba.drive_direct(self.power,-self.power)
        else:
            roomba.drive_direct(self.power,self.power)
        #Will add expected turning amounts, later.

    def get_depth(self):
        return freenect.sync_get_depth()[0]
    
    def get_depth_transposed(self):
        return get_depth().transpose()    

