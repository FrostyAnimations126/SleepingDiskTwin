class SleepingDisk:
    def __init__(self):
        self.powerstate=0
        self.position=0
    def WakeUp(self):
        wait(random(2,10))
        self.powerstate=1
    def Read(self,pos):
        if self.powerstate==0:
            self.WakeUp()
        self.position=pos
        return
    def Write(self,pos,data):
        if self.powerstate==0:
            self.WakeUp()
        self.position=pos
        return
    def Sleep(self):
        self.powerstate=0
        return
    
print("Mounting disk")
disk = SleepingDisk()
print("Reading file from idle disk")
data = disk.Read(100)
print("Got data")
print("Writing file to idle disk")
disk.Write(100, data)
print("Done")