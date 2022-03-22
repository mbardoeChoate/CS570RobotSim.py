import pygame
from pygame.locals import *
import robot
WHITE = (255, 125, 255)

DOOFUS EOFError


class RobotView(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, surface,color, myRobot):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.color=color
        self.screen=surface
        self.robot=myRobot

        # Draw the car (a rectangle!)
        #pygame.draw.rect(self.image, color, [0, 0, self.robot.width, self.robot.height])

        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        #self.rect = self.image.get_rect()

    def create_Image(self):
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.surf = pygame.Surface([self.robot.width+20, self.robot.height])
        self.surf = self.surf.convert_alpha()
        self.surf.fill((0, 0, 0, 0))
        self.RobotBody=pygame.draw.rect(self.surf, self.color, Rect(10, 0, self.robot.width, self.robot.height))
        self.left_front_wheel=pygame.draw.rect(self.surf, (0,255,0), Rect(0,3,10,3))
        self.right_front_wheel=pygame.draw.rect(self.surf, (0,255,0), Rect(self.robot.width+10,3,10,3))
        self.left_back_wheel=pygame.draw.rect(self.surf, (0,255,0), Rect(0,self.robot.height-3,10,3))
        self.right_back_wheel=pygame.draw.rect(self.surf, (0,255,0), Rect(self.robot.width+10,self.robot.height-3,10,3))
