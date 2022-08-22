from math import sqrt
  

class Point:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "".join(["(", str(self.x), ", ", str(self.y), ")"])

    def __repr__(self):
        return "".join(["Point(", str(self.x), ", ", str(self.y), ")"])

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_from(self, pt):
        return sqrt((self.x - pt.x)**2 + (self.y - pt.y)**2)
