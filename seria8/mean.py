from abc import ABC, abstractmethod
import sys

class Mean(ABC):
    def __init__(self, x: list) -> None:
        self.x = x
    
    def n(self) -> int:
        return len(self.x)
    
    @abstractmethod
    def __call__(self):
        pass


class ArithmeticMean(Mean):
    def __call__(self) -> float:
        return sum(self.x)/len(self.x)
    

class GeometricMean(Mean):
    def __call__(self) -> float:
        result = 1
        for element in self.x:
            result *= element
        return result**(1/self.n())


class HarmonicMean(Mean):
    def __call__(self):
        return self.n()/(sum([1/element for element in self.x]))
    

if __name__ == "__main__":
    lista = []
    for line in sys.stdin:
        if line.rstrip() == 'q':
            break
        lista.append(int(line))
    
    amean = ArithmeticMean(lista)
    gmean = GeometricMean(lista)
    hmean = HarmonicMean(lista)

    print(amean(), gmean(), hmean())