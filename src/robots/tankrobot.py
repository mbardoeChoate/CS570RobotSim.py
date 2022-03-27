from src.robots.robot import Robot
from src.drivetrains.tankdrivetrain import TankDriveTrain


class TankRobot(Robot):

    def __init__(self, width, height, direction, position):
        super(TankRobot, self).__init__(width, height, direction, position)
        self.drive_train = TankDriveTrain()

    def run(self):
        self.drive_train(self.center_position[0], self.center_position[1], self.direction)
