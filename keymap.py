"""
Basic keymap usage.
"""
from settings.colors import Color
from settings.config import RUNNING, SCREEN_CONF
from tools.utils import PyGame


with PyGame() as pygame:
    # Set screen size.
    screen = pygame.display.set_mode(SCREEN_CONF)
    # Set default background color.
    background = Color.black
    while RUNNING:
        # Event loop, to cat the keymap activity.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    background = Color.green
                elif event.key == pygame.K_k:
                    background = Color.red

        # Set the screen color.
        screen.fill(background)
        pygame.display.update()
