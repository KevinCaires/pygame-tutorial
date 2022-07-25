"""
Drawing rectangle in screen.
"""
from tools.utils import PyGame
from settings.colors import Color
from settings.config import *

with PyGame() as pygame:
    screen = pygame.display.set_mode(SCREEN_CONF)
    x = 50
    y = 60
    w = 200
    h = 80
    left = 50
    top = 60
    right = 250
    bottom = 140
    center = (150, 100)
    rect = pygame.Rect(left, right, w, h)

    print(f'x={rect.x}, y={rect.y}, w={rect.w}, h={rect.h}')
    print(f'left={rect.left}, top={rect.top}, right={rect.right}, bottom={rect.bottom}')
    print(f'center={rect.center}')

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        screen.fill(Color.grey)
        pygame.draw.rect(screen, Color.red, rect)
        pygame.display.flip()  # Draw in screen.
