
class Motor(object):

    def __init__(self):
        self.encoder_per_rev =255
        self.encoder=0
        self.voltage=0
        self.gearing=255 # how many revolutions at max voltage

    def set_Voltage(self,voltage):
        self.voltage=max(0,min(1,voltage)) # keep between 0 and 1

    def run(self,dt):
        revolutions=self.voltage*self.gearing*dt
        self.encoder+= self.encoder_per_rev * revolutions
        return revolutions