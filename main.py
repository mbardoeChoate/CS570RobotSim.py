import pygame
from src.robots import robot
from src.robots.robotviews import robotView
from src.etc.eventhandler import EventHandler


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Main:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.running = True
        self.eventhandler = EventHandler(self)
        self.create_display()
        self.draw_background()
        self.add_robot()
        self.run()

    def create_display(self):
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("CS570 Robot Sim")

    def draw_background(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((255, 255, 255))

    def add_robot(self):
        self.my_robot = robot.Robot(40, 40, 1, (200, 100))
        self.my_robotView = robotView.RobotView(self.screen, (255, 125, 255), self.my_robot)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.eventhandler.handle_event(event)

            self.screen.blit(self.background, (0, 0))
            self.my_robotView.create_Image()
            # rotSurf = pygame.transform.rotate(Player.surf, Player.angle)
            self.screen.blit(self.my_robotView.surf,
                             self.my_robotView.surf.get_rect(center=self.my_robot.center_position))
            self.my_robot.run()
            # Flip the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()


if __name__ == "__main__":
    main = Main()
