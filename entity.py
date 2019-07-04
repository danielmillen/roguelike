class Entity:
    """
    A generic object to represent players, items, enemies, etc.
    """
    def __init__(self, x, y, char, color, player=False):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.player = player

    def move(self, dx, dy):
        # Move the entity by the given amount
        self.x += dx
        self.y += dy
