from src.robots.robot import Robot
from src.drivetrains.tankdrivetrain import TankDriveTrain


class TankRobot(Robot):

    def __init__(self, width, height, direction, position):
        super(TankRobot, self).__init__(width, height)
        self.drivetrain = TankDriveTrain(direction, position)

    def run(self):
        self.drivetrain.run()
        # self.center_position = (x, y)
        # self.direction = d
