from drivetrain import Drivetrain
from src.robots.robotparts.motor import Motor
from unum.units import cm, s
from src.etc.constants import TIME_STEP
import math


class TankDriveTrain(Drivetrain):

    def __init__(self):
        super(TankDriveTrain, self).__init__(2, 4 * cm)
        self.left_motor = self.motors[0]
        self.right_motor = self.motors[1]
        self.left_wheel = self.wheels[0]
        self.right_wheel = self.wheels[1]

    def run(self, x, y, angle):
        '''This method gives the amount of change in x, y, and theta for with the current
        setting of the motors for one TIME_STEP'''
        lv = self.left_motor.revolutions(TIME_STEP) * self.left_wheel.wheel_circumference
        rv = self.right_motor.revolutions(TIME_STEP) * self.left_wheel.wheel_circumference
        ld = lv * TIME_STEP
        rd = rv * TIME_STEP
        if lv == rv:
            ld = lv * TIME_STEP
            return x + ld * math.sin(math.pi / 2.0 - angle), y + ld * math.sin(math.pi / 2.0 - angle), angle
        else:
            radius_rotation = (rd * self.drive_base) / (ld - rd)
            d_theta = rd / radius_rotation
            movement_angle = (math.pi - d_theta) / 2.0
            dy = radius_rotation * math.sin(d_theta)
            dx = dy / math.tan(movement_angle)
            return x + dx, y + dy, angle - d_theta
