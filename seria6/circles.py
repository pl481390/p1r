import math
import argparse
from typing import Self

class Circle:
    def __init__(self, x: float, y: float, r: float):
        self.x = x
        self.y = y
        self.r = r
    
    def circumference(self):
        c = 2*math.pi*self.r
        return c
    
    def _odleglosc_srodkow(self, other: Self):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
    
    def intersection(self, other: Self):
        odleglosc = self._odleglosc_srodkow(other)
        if odleglosc > self.r+other.r:
            return 0
        elif odleglosc == 0:
            if self.r == other.r:
                return math.inf
            else:
                return 0
        elif odleglosc + self.r == other.r or odleglosc + other.r == self.r or odleglosc == self.r + other.r:
            return 1
        else:
            return 2
        """elif odleglosc == self.r+other.r and odleglosc != 0:
            return 1
        else:
            if odleglosc + self.r == other.r or odleglosc + other.r == self.r:
                return 1
            elif odleglosc + self.r < other.r or odleglosc + other.r < self.r:
                return 0
            elif odleglosc == 0 and self.r == other.r:
                return math.inf
            else:
                return 2"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("x1", type=float)
    parser.add_argument("y1", type=float)
    parser.add_argument("r1", type=float)
    parser.add_argument("x2", type=float)
    parser.add_argument("y2", type=float)
    parser.add_argument("r2", type=float)
    args = parser.parse_args()

    circle1 = Circle(args.x1, args.y1, args.r1)
    circle2 = Circle(args.x2, args.y2, args.r2)

    print("Obwody:", circle1.circumference(), circle2.circumference())
    print("Liczba punktów wspólnych:", circle1.intersection(circle2))