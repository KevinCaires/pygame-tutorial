"""
Game general configurations.
"""
from pygame.locals import *

from settings.colors import Color

# Control the running screen.
RUNNING = True
# Screen lenght configuration.
SCREEN_CONF = (800, 600)
# Key dict to facility the key-color mapping.
KEY_COLOR_DICT = {
    K_k: Color.black,
    K_r: Color.red,
    K_g: Color.green,
    K_b: Color.blue,
    K_y: Color.yellow,
    K_c: Color.cyan,
    K_m: Color.magenta,
    K_w: Color.white,
}
