from src.robots.robotparts.wheel import Wheel
from unum.units import cm

class Robot(object):

    def __init__(self, width, height, direction, position):
        self.width = width * cm
        self.height = height * cm
        self.direction = direction  # direction in radians 0 is up
        self.center_position = position
        self.left_front_wheel = Wheel(4)
        self.left_back_wheel = Wheel(4)
        self.right_front_wheel = Wheel(4)
        self.right_back_wheel = Wheel(4)
        self.drivetrain = None

    def set_motor_voltage(self, motor_num, value):
        self.drivetrain.motors[motor_num].set_voltage(value)

    def run(self):
        '''You must create a drivetrain.'''
        # This is where the logic of how the motors cause the robot to move will be.
        # self.center_position=(self.center_position[0], self.center_position[1]+.2)
        # self.direction+=.02
        pass
