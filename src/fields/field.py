from unum import Unum, cm
from pygame import display, image


class Field:
    background = 0
    screen = 0

    def __init__(self, width, height, distance_conversion):
        super().__init__()
        self.screen = display.set_mode([width, height])
        # self.background = image.load("2022 frc fields.png")
        # self.background.set_alpha(100)
        #self.screen.blit(self.background, self.background.get_rect())
        self.distance_conversion=Unum.unit("mypx", cm/distance_conversion)
        display.update()
        # print(background.get_rect())


    def background_refresh(self):
        display.update()


    def clear(self):
        self.screen.fill([0, 0, 0])
        #self.screen.blit(self.background, self.background.get_rect())
        display.update()


    def return_screen(self):
        return self.screen