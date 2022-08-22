from point import Point
import math

class Circle:
    r = 0

    def __init__(self, c=None, r=1):
        if c is None:
            self.c = Point(0, 0)
        else:
            self.c = c
        self.r = r
        if(self.r < 0):
            raise ValueError("Radius must be greater than or equal to zero")
        else:
            pass


    def __str__(self):
        return "".join(["(",  str(self.c), ", ", str(self.r), ")"])

    def __repr__(self):
        return "".join(["Circle(", str(self.c), ", ", str(self.r), ")"])

    def move(self, dx, dy):
        self.c.move(dx, dy)


    def intersection_area(self, other_circle):
        d = math.sqrt((other_circle.c.x - self.c.x)**2 + (other_circle.c.y - self.c.y)**2)

        if(d < self.r + other_circle.r):
            a = self.r*self.r
            b = other_circle.r * other_circle.r

            if(d <= abs(other_circle.r - self.r) or d == 0):
                return math.pi * min(a, b)

            x = (a-b+d*d)/(2*d)
            y = (b-a+d*d)/(2*d)
            z = 0.5*math.sqrt((-d+self.r+other_circle.r)*(d+self.r-other_circle.r)*(d-self.r+other_circle.r)*(d+self.r+other_circle.r))

            return a*math.acos(x/self.r) + b*math.acos(y/other_circle.r) - z
        return 0


#p1 = Point(0, 0)
#c1 = Circle(p1, 1)

#p2 = Point(0, 0)
#c2 = Circle(p2, 10)
#print(c2.intersection_area(c1))
