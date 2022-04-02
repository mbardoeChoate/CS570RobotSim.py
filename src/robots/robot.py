from src.robots.robotparts.wheel import Wheel
from unum.units import cm

class Robot(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.drivetrain = None

    def add_drivetrain(self, drivetrain):
        self.drivetrain = drivetrain

    def set_motor_voltage(self, motor_num, value):
        self.drivetrain.motors[motor_num].set_voltage(value)

    def get_surface_position(self):
        return (self.drivetrain.pose.X().asNumber(m), self.drivetrain.pose.Y().asNumber(cm))

    def run(self):
        '''You must create a drivetrain.'''
        # This is where the logic of how the motors cause the robot to move will be.
        # self.center_position=(self.center_position[0], self.center_position[1]+.2)
        # self.direction+=.02
        pass
