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
