from unum.units import cm
from pygame import display, image
from unum import Unum


class Field:
    background = None
    screen = None

    def __init__(self, width, height, distance_conversion):
        super().__init__()
        self.screen = display.set_mode([width, height])
        display.set_caption("CS570 Robot Sim")
        self.distance_conversion = Unum.unit("mypx", 1 / distance_conversion * cm)
        display.update()

    def draw_background(self):
        self.screen.fill([255, 255, 255])

    def background_refresh(self):
        display.update()

    def clear(self):
        self.screen.fill([0, 0, 0])
        # self.screen.blit(self.background, self.background.get_rect())
        display.update()

    def return_screen(self):
        return self.screen