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
    rect_list = []

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == MOUSEBUTTONDOWN:
                start = event.pos
                size = 0, 0
                drawing = True
            elif event.type == MOUSEBUTTONUP:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                rect = pygame.Rect(start, size)
                rect_list.append(rect)
                drawing = False
            elif event.type == MOUSEMOTION and drawing:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]

        screen.fill(Color.grey)

        for rect in rect_list:
            pygame.draw.rect(screen, Color.red, rect, 3)

        pygame.draw.rect(screen, Color.blue, (start, size), 1)
        pygame.display.update()
