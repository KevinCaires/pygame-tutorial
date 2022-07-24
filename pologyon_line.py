"""
Drawing rectangle in screen.
"""
from tools.utils import PyGame
from settings.colors import Color
from settings.config import *

with PyGame() as pygame:
    screen = pygame.display.set_mode(SCREEN_CONF)
    start = (0, 0)
    size = (0, 0)
    drawing = False
    points = []

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == MOUSEBUTTONDOWN:
                points.append(event.pos)
                drawing = True
            elif event.type == MOUSEBUTTONUP:
                drawing = False
            elif event.type == MOUSEMOTION and drawing:
                points[-1] = event.pos
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if len(points) > 0:
                        points.pop() 

        screen.fill(Color.white)

        if len(points) > 1:
            rect = pygame.draw.lines(screen, Color.red, True, points, 3)
            pygame.draw.rect(screen, Color.green, rect, 1)

        pygame.display.update()
