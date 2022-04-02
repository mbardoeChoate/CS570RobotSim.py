from unum.units import cm, s
from unum import Unum

my_px = Unum.unit("my_px", 1700.0 / 648.0 / 2.54 * cm)
inch = Unum.unit("inch", 2.54 * cm)
TIME_STEP = 0.02 * s
WIDTH_2022 = 1700
HEIGHT_2022 = 850
FPS = 50
