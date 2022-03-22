import pygame
import robot, robotView
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
my_robot=robot.Robot(20,20,0,(100,100))
my_robotView=robotView.RobotView(screen, (255,125,255),my_robot )
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    my_robotView.create_Image()
    #rotSurf = pygame.transform.rotate(Player.surf, Player.angle)
    screen.blit(my_robotView.surf, my_robotView.surf.get_rect(center = my_robot.center_position))
    my_robot.run()
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
