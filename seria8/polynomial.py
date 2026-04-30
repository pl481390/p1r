import argparse
from typing import Self

def hermite_coeffs(n: int) -> list:
    from sympy import hermite, Poly, Symbol
    x = Symbol('x')
    return Poly(hermite(n, x), x).coeffs()[::-1]

def legendre_coeffs(n: int) -> list:
    from sympy import legendre, Poly, Symbol
    x = Symbol('x')
    return Poly(legendre(n, x), x).coeffs()[::-1]


class Polynomial:
    c =[]

    def __init__(self, coeffs: list) -> None:
        while coeffs[-1] == 0:
            coeffs.pop()
        self.c = coeffs
    
    def deg(self) -> int:
        return len(self.c) - 1
    
    def __add__(self, other: "Polynomial") -> "Polynomial":
        coeffs = [0]*max(len(self.c), len(other.c))
        for n,a in enumerate(self.c):
            coeffs[n] += a
        for n,a in enumerate(other.c):
            coeffs[n] += a
        return Polynomial(coeffs)
    
    def __call__(self, x: float) -> float:
        result = 0
        for i in range(len(self.c)):
            result += self.c[i]*x**i
        return result
    
    def __mul__(self, a: float) -> "Polynomial":
        coeffs = [a*coeff for coeff in self.c]
        return Polynomial(coeffs)
    
    def __rmul__(self, a: float) -> "Polynomial":
        coeffs = [a*coeff for coeff in self.c]
        return Polynomial(coeffs)
    
    def derrivative(self) -> "Polynomial":
        coeffs = [0]*len(self.c)
        for i in range(1, len(self.c)):
            coeffs[i-1] = i*self.c[i]
        return Polynomial(coeffs)


class HermitePolynomial(Polynomial):
    def __init__(self, n: int) -> None:
        Polynomial.__init__(self, hermite_coeffs(n))


class LegendrePolynomial(Polynomial):
    def __init__(self, n: int) -> None:
        Polynomial.__init__(self, legendre_coeffs(n))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("x", type=float)
    args = parser.parse_args()

    hermite = HermitePolynomial(args.n)
    legendre = LegendrePolynomial(args.n)
    hermite_d = hermite.derrivative()
    legendre_d = legendre.derrivative()

    print(hermite(args.x))
    print(legendre(args.x))
    print(hermite_d(args.x) + legendre_d(args.x) + 3*(hermite(args.x)+legendre(args.x)))