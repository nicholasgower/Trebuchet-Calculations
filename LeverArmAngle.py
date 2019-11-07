import math
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:52:18 2019

@author: nicholas
"""

#Constants
g=9.80665
class world:
    def __init__():
        self.deltaTime=0.01 #Amount of time simulated in each loop
        self.things=[leverArm()] #Unneccessary amount of generalization, but why not be general?
        
    def simulate(totalTime=10):
        time=0
        while time<totalTime:
            
            print("Current time:{} s".format(time))
            for thing in self.things:
                thing.update(self.deltaTime)
                if thing.angle is not None:
                    print("Angle of {}:{}".format(thing.name,thing.angle))
                if thing.angularVel is not None:
                    print("Anglular Velocity of {}:{}".format(thing.name,thing.angularVel))
                if thing.angularVel is not None:
                    print("Anglular Acceleration of {}:{}".format(thing.name,thing.angularAcc))
            time+=self.deltaTime
class leverArm:
    def __init__(name="New lever arm",L1=12,L2=6):
        self.name=name
        self.angle=math.radians(45) #Radians
        self.angularVel=0 #Rad/s
        self.angularAcc=0 #Rad/s^2
        self.L1=L1
        self.L2=L2
    def update(deltaTime):
        self.angularAcc=(g*math.sin(self.angle))/L1
        self.angularVel+=deltaTime*self.angularAcc
        self.angle+=deltaTime*self.angularVel