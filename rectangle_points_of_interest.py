"""
Drawing rectangle, points of interest.
"""
from settings.colors import Color
from settings.config import *
from tools.utils import PyGame

with PyGame() as pygame:
    pts = (
        'topleft',
        'topright',
        'bottomleft',
        'bottomright',
        'midtop',
        'midright',
        'midbottom',
        'midleft',
        'center'
    )
    screen = pygame.display.set_mode(SCREEN_CONF)
    rect = pygame.Rect(50, 250, 200, 80)
    font  = pygame.font.Font('fonts/zabal/ZabalDEMO-Medium.otf', 12)


    while RUNNING:
        for event in pygame.event.get():
            if event.type == QUIT:
                RUNNING = False

        screen.fill(Color.white)
        pygame.draw.rect(screen, Color.green, rect,4)

        for pt in pts:
            pos = eval(f'rect.{pt}')
            # Resonvendo a parte que o módulo citado não funciona.
            screen.blit(font.render(pt, False, Color.black), pos)
            pygame.draw.circle(screen, Color.red, pos, 3)

        pygame.display.flip()
