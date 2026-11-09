from datetime import datetime
import time
import random
def wait(sec):
    time.sleep(sec)

class SleepingDisk:
    def __init__(self):
        self.powerstate=0
        self.position=0
        self.id=random.randint(1000,9999)
        self.start=0
    def WakeUp(self):
        wait(random.randint(2,10))
        self.powerstate=1
        self.start=datetime.now()
    def Read(self,pos):
        if self.powerstate==0:
            self.WakeUp()
            
        wait(random.randint(0,3))
        self.position=pos
        return
    def Write(self,pos,data):
        if self.powerstate==0:
            self.WakeUp()
        wait(random.randint(0,3))
        self.position=pos
        return
    def Sleep(self):
        self.powerstate=0
        return
    def GetRuntime(self):
        if self.powerstate==0:
            return 0
        else:
            return (datetime.now()-self.start).total_seconds()
    
print("Mounting disk")
disk = SleepingDisk()
print("Disk id: ", disk.id)
print("Reading file from idle disk")
data = disk.Read(100)
print("Got data")
print("Writing file to idle disk")
disk.Write(100, data)
print("Done")
print("Disk has been online for", disk.GetRuntime(), "seconds")
disk.Sleep()
print("Finished")
