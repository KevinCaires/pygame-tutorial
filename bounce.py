"""
Ball animation script.
"""
from settings.colors import Color
from settings.config import RUNNING, SCREEN_CONF
from tools.utils import PyGame

WIDTH, HEIGHT = SCREEN_CONF

with PyGame() as pygame:
    screen = pygame.display.set_mode(SCREEN_CONF)
    ball = pygame.image.load('images/ball.gif')
    rect = ball.get_rect()
    speed = [2, 2]

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        # Control the corner colide.
        rect = rect.move(speed)
        if rect.left < 0 or rect.right > WIDTH:
            speed[0] = -speed[0]
        if rect.top < 0 or rect.bottom > HEIGHT:
            speed[1] = -speed[1]

        screen.fill(Color.green)
        pygame.draw.rect(screen, Color.red, rect, 1)
        screen.blit(ball, rect)
        pygame.display.update()
