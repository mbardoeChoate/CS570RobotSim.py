import math

import pygame
from src.robots import robot
from src.robots import tankrobot
from src.drivetrains.tankdrivetrain import TankDriveTrain
from src.robots.robotviews import robotView
from src.etc.eventhandler import EventHandler
from src.etc.constants import WIDTH_2022, HEIGHT_2022
from src.fields.field_2022 import Field_2022
from src.fields.field import Field
from src.etc.constants import FPS, inch
from unum.units import cm, rad, deg


######
# Note: wpilib is oriented so that the angle is the in the x direction
#

class Main:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.screen_width = WIDTH_2022
        self.screen_height = HEIGHT_2022
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.running = True
        self.field = Field_2022()
        # self.field = Field(1700, 850, 1700.0 / 648.0 * 2.54)
        self.fps = FPS  # because the robot updates every 0.02 seconds
        self.eventhandler = EventHandler(self)
        self.draw_background()
        self.add_robot()
        self.run()

    def draw_background(self):
        self.field.draw_background()

    def add_robot(self):
        self.my_robot = tankrobot.TankRobot(40 * 2.54 * cm, 40 * 2.54 * cm, math.pi * rad, (200, 100))
        self.drivetrain = TankDriveTrain(1, (200, 100))
        self.my_robot.add_drivetrain(self.drivetrain)
        self.my_robot.set_motor_voltage(0, 1)
        self.my_robot.set_motor_voltage(1, 1)
        self.my_robotView = robotView.RobotView(self.field.screen, (255, 125, 255), self.my_robot)

    def update_screen(self):
        self.screen.blit(self.field.screen, (0, 0))
        self.my_robotView.create_Image()
        transformed_position = (self.drivetrain.pose.X(), self.drivetrain.pose.Y())
        self.screen.blit(self.my_robotView.surf,
                         self.my_robotView.surf.get_rect(center=transformed_position))
        text = self.font.render(str(pygame.time.get_ticks() / 1000.0), True, (255, 0, 0))
        textRect = text.get_rect()
        textRect.center = (80, self.screen_height - 50)
        self.screen.blit(text, textRect)

    def run(self):
        self.clock = pygame.time.Clock()
        while self.running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                self.eventhandler.handle_event(event)
            self.update_screen()  # update the sreen
            pygame.display.flip()  # Flip the display
            self.my_robot.run()  # move the game forward
        pygame.quit()  # Done! Time to quit.


if __name__ == "__main__":
    main = Main()
