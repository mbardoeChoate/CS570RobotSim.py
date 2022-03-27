from src.robots.robot import Robot
from src.drivetrains.tankdrivetrain import TankDriveTrain


class TankRobot(Robot):

    def __init__(self, width, height, direction, position):
        super(TankRobot, self).__init__(width, height, direction, position)
        self.drivetrain = TankDriveTrain()

    def run(self):
        x, y, d = self.drivetrain.run(self.center_position[0], self.center_position[1], self.direction)
        self.center_position = (x, y)
        self.direction = d
