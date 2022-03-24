from wheel import Wheel
from unum.units import cm
class Robot(object):

    def __init__(self,width,height,direction,position):
        self.width=width * cm
        self.height=height * cm
        self.direction=direction # direction in radians 0 is up
        self.center_position=position
        self.left_front_wheel = Wheel()
        self.left_back_wheel = Wheel()
        self.right_front_wheel = Wheel()
        self.right_back_wheel = Wheel()

    def run(self):
        self.center_position=(self.center_position[0], self.center_position[1]+.2)
        self.direction+=.02