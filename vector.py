class Vector(object):
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __iter__(self):
        return iter((self.x, self.y))