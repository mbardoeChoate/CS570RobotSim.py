from unum.units import s
class Motor(object):

    def __init__(self):
        self.encoder_per_rev = 256
        self.encoder = 0
        self.voltage = 0
        self.gearing = 72  # how many revolutions at max voltage

    def set_voltage(self, voltage):
        self.voltage = max(-1, min(1, voltage))  # keep between 0 and 1

    def revolutions(self):
        revolutions = self.voltage * self.gearing
        self.encoder += self.encoder_per_rev * revolutions
        return revolutions * 1 / s
