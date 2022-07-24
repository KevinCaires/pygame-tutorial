"""
Basic graph.
"""
from settings.colors import Color
from settings.config import KEY_COLOR_DICT, RUNNING, SCREEN_CONF
from tools.utils import PyGame

BACKGROUND = Color.grey

with PyGame() as pygame:
    screen = pygame.display.set_mode(SCREEN_CONF)

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                # Set BACKGROUND by color key map.
                if event.key in KEY_COLOR_DICT:
                    BACKGROUND = KEY_COLOR_DICT.get(event.key)
                    # Set header
                    pygame.display.set_caption(f'background color {str(BACKGROUND)}')

        screen.fill(BACKGROUND)
        # Draw ellipse.
        # _ColorValue: RGB
        # _RectValue: object
        pygame.draw.ellipse(screen, Color.red, (50, 20, 160, 100))
        pygame.draw.ellipse(screen, Color.green, (100, 60, 160, 100))
        pygame.draw.ellipse(screen, Color.blue, (150, 100, 160, 100))

        # Another ellipse drawing.
        pygame.draw.ellipse(screen, Color.red, (350, 20, 160, 100), 1)
        pygame.draw.ellipse(screen, Color.green, (400, 60, 160, 100), 4)
        pygame.draw.ellipse(screen, Color.blue, (450, 100, 160, 100), 8)
        pygame.display.update()
