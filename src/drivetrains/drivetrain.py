from src.robots.robotparts.motor import Motor
from src.robots.robotparts.wheel import Wheel
from unum.units import cm, m
from wpimath.kinematics import DifferentialDriveOdometry
from wpimath.geometry import Pose2d, Rotation2d


class Drivetrain():
    motors = []
    wheels = []

    def __init__(self, num_motors, drive_base, wheel_cirumference, direction, position):
        super(Drivetrain, self).__init__()
        self.pose = Pose2d(x=position[1], y=position[0], angle=-direction)
        self.num_motors = num_motors
        for i in range(num_motors):
            self.motors.append(Motor())
        for i in range(num_motors):
            self.wheels.append(Wheel(wheel_cirumference))
        self.drive_base = drive_base * cm

    def add_motor(self, pos, motor):
        self.motors[pos] = motor

    def set_motor_voltage(self, pos, value):
        self.motors[pos].set_voltage(value)

    def get_motor_revs(self, pos):
        return self.motors[pos].revolutions()

    def run(self):
        pass
