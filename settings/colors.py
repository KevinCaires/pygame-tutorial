"""
Colors definition.
"""

class Color:
    """
    Return RGB tuple.
    """
    black = (0, 0, 0)
    grey = (127, 127, 127)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    cyan = (0, 255, 255)
    magenta = (255, 0, 255)

    @classmethod
    def to_tuple(self) -> tuple:
        return (
            self.black,
            self.grey,
            self.white,
            self.red,
            self.green,
            self.blue,
            self.yellow,
            self.cyan,
            self.magenta,
        )
