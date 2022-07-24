"""
Basic usage and funcionalits test.
"""
import pygame

class PyGame:
    """
    pygame context manager.
    """
    def __init__(self) -> None:
        """
        Initialize interface.
        """
        pygame.init()

    def __enter__(self) -> pygame:
        """
        Pygame object.
        """
        return pygame

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Exit interface.
        """
        pygame.quit()
