from unum.units import cm
from src.robots.robotparts.motor import Motor

class Wheel(object):

    def __init__(self, wheel_circumference):
        self.motor = Motor()
        self.wheel_circumference = wheel_circumference * cm

    def run(self):
        pass




