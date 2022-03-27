import pygame
from src.robots import robot
from src.robots import tankrobot
from src.robots.robotviews import robotView
from src.etc.eventhandler import EventHandler


class Main:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.running = True
        self.fps = 50  # because the robot updates every 0.02 seconds
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
        self.my_robot = tankrobot.TankRobot(40, 40, 1, (200, 100))
        self.my_robotView = robotView.RobotView(self.screen, (255, 125, 255), self.my_robot)

    def update_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.my_robotView.create_Image()
        # rotSurf = pygame.transform.rotate(Player.surf, Player.angle)
        self.screen.blit(self.my_robotView.surf,
                         self.my_robotView.surf.get_rect(center=self.my_robot.center_position))

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
