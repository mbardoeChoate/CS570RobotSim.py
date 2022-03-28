from unum import Unum
from unum.units import cm
from pygame import image

inch = Unum.unit("inch", 2.54 * cm)
from src.fields.field import Field


class Field_2022(Field):

    def __init__(self):
        super(Field_2022, self).__init__(1700, 850, 1700.0 / 648.0 * 2.54)
        self.background = image.load("img/2022-field.png")
        self.draw_background()

    def draw_background(self):
        self.screen.blit(self.background, self.background.get_rect())
