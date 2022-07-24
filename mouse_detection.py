from random import choice

from settings.colors import Color
# KEY_COLOR_DICT, RUNNING, SCREEN_CONF and locals of pygame.
from settings.config import *
from tools.utils import PyGame

BACKGROUND = Color.grey

with PyGame() as pygame:
    screen = pygame.display.set_mode(SCREEN_CONF)

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == MOUSEBUTTONDOWN:
                BACKGROUND = Color.black
            elif event.type == MOUSEBUTTONUP:
                BACKGROUND = Color.blue
            elif event.type == MOUSEMOTION:
                colors = Color.to_tuple()
                BACKGROUND = choice(colors)

        screen.fill(BACKGROUND)
        pygame.display.update()
        