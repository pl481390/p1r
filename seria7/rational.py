import argparse
import math

class RationalNumber:
    def __init__(self, p : int = 0, q : int = 1) -> None:
        if q==0:
            raise ZeroDivisionError
        self.p = p
        self.q = q
        if self.q < 0:
            self.p = -p
            self.q = -q
        if math.gcd(p, q) > 1:
            self.p /= math.gcd(p, q)
            self.q /= math.gcd(p, q)
    
    def numerator(self) -> int:
        return self.p
    
    def denominator(self) -> int:
        return self.q
    
    def __float__(self) -> float:
        return self.p/self.q
    
    def __neg__(self):
        self.p = -self.p
        return self
    
    def __lt__(self, other : "RationalNumber") -> bool:
        return self.p*other.q < other.p*self.q
    
    def __add__(self, other : "RationalNumber") -> "RationalNumber":
        return RationalNumber(self.p*other.q + other.p*self.q, self.q*other.q)
    
    def __sub__(self, other : "RationalNumber") -> "RationalNumber":
        return self + (-other)
    
    def __mul__(self, other : "RationalNumber") -> "RationalNumber":
        return RationalNumber(self.p*other.p, self.q*other.q)
    
    def __truediv__(self, other : "RationalNumber") -> "RationalNumber":
        return RationalNumber(self.p*other.q, self.q*other.p)
    
    def __iadd__(self, other : "RationalNumber"):
        self = self + other
        return self
    
    def __isub__(self, other : "RationalNumber"):
        self = self - other
        return self
    
    def __imul__(self, other : "RationalNumber"):
        self = self * other
        return self
    
    def __itruediv__(self, other : "RationalNumber"):
        self = self / other
        return self
    
    def __repr__(self) -> str:
        return f"RationalNumber({self.p}, {self.q})"
    
    def __str__(self) -> str:
        return f"{self.p}/{self.q}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fraction1", type=str)
    parser.add_argument("fraction2", type=str)
    wczytane = parser.parse_args

    print(wczytane.fraction1)
    """args1 = [int(x) for x in input.fraction1.split("/")]
    args2 = [int(x) for x in input.fraction2.split("/")]
    rational1 = RationalNumber(*args1)
    rational2 = RationalNumber(*args2)

    print(float(rational1), float(rational2))
    print(-rational1, -rational2)
    sorted_list = sorted([rational1, rational2])
    print(sorted_list[0], sorted_list[1])
    print(rational1+rational2, rational1*rational2)"""