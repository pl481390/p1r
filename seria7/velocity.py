import math
from typing import Self
import argparse

class Velocity:
    def __init__(self, velocity : float = 0) -> None:
        self.velocity = velocity
    
    def gamma(self) -> float:
        return 1/(math.sqrt(1-self.velocity**2))
    
    def __add__(self, other: "Velocity") -> "Velocity":
        b1 = self.velocity
        b2 = other.velocity
        return Velocity((b1+b2)/(1+b1*b2))
    
    def __iadd__(self, other: "Velocity"):
        b1 = self.velocity
        b2 = other.velocity
        self.velocity = (b1+b2)/(1+b1*b2)
        return self
    
    def __str__(self) -> str:
        return f"beta = {self.velocity} \ngamma = {self.gamma()}"
    
    def __repr__(self) -> str:
        return f"Velocity({self.velocity})"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("v1", type=float)
    parser.add_argument("v2", type=float)
    args = parser.parse_args()

    velocity1 = Velocity(args.v1)
    velocity2 = Velocity(args.v2)

    print(velocity1+velocity2)