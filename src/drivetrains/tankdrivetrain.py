from src.drivetrains.drivetrain import Drivetrain
from src.robots.robotparts.motor import Motor
from unum.units import cm, s, m
from src.etc.constants import TIME_STEP
import math
from wpimath.kinematics import DifferentialDriveOdometry
from wpimath.geometry import Pose2d, Rotation2d


class TankDriveTrain(Drivetrain):

    def __init__(self, my_angle, position):
        super(TankDriveTrain, self).__init__(2, 35, 6, my_angle, position)
        self.left_motor = self.motors[0]
        self.right_motor = self.motors[1]
        self.left_wheel = self.wheels[0]
        self.right_wheel = self.wheels[1]
        self.odometry = DifferentialDriveOdometry(Rotation2d(-my_angle),
                                                  Pose2d(position[0], position[1], Rotation2d(-my_angle)))

    def get_motor_velocity(self, pos):
        return self.motors[pos].revolutions() * self.wheels[pos].wheel_circumference * 2 * math.pi

    def gyro_sim(self):
        # Returns the rate of angle change
        angle = (self.get_motor_velocity(1) - self.get_motor_velocity(0)) / self.drive_base
        # angle = (1.0/.02 *cm/s- 1.1/.02 *cm/s) / self.drive_base
        return angle

    def run(self):
        # self.odometry.resetPosition(Pose2d(x.asNumber(m),y.asNumber(m), angle), -Rotation2d(angle))
        lv = self.get_motor_velocity(0)
        rv = self.get_motor_velocity(1)
        ld = lv * TIME_STEP
        rd = rv * TIME_STEP
        self.pose = self.odometry.update(self.pose.rotation(), ld.asNumber(m), rd.asNumber(m))
        new_rotation = Rotation2d(self.pose.rotation().radians() + TIME_STEP * self.gyro_sim())
        self.odometry.resetPosition(self.pose, new_rotation)

    # def run(self, x, y, angle):
    #     '''This method gives the amount of change in x, y, and theta for with the current
    #     setting of the motors for one TIME_STEP'''
    #     lv = self.left_motor.revolutions() * self.left_wheel.wheel_circumference
    #     rv = self.right_motor.revolutions() * self.left_wheel.wheel_circumference
    #     ld = lv * TIME_STEP
    #     rd = rv * TIME_STEP
    #     if lv == rv:
    #         ld = lv * TIME_STEP
    #         return x + ld * math.sin(math.pi / 2.0 - angle), y + ld * math.sin(math.pi / 2.0 - angle), angle
    #     else:
    #         radius_rotation = (rd * self.drive_base) / (ld - rd)
    #         d_theta = rd / radius_rotation
    #         movement_angle = (math.pi - d_theta) / 2.0
    #         unrotated_dy = -(radius_rotation + self.drive_base / 2.0) * math.sin(d_theta)
    #         unrotated_dx = (radius_rotation + self.drive_base / 2.0) * (1 - math.cos(d_theta))
    #         dx = math.cos(angle) * unrotated_dx + math.sin(angle) * unrotated_dy
    #         dy = -math.sin(angle) * unrotated_dx + math.cos(angle) * unrotated_dy
    #         return x + dx, y + dy, angle - d_theta
