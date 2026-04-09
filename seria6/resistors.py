import argparse

class Resistor:
    def __init__(self, R: float = 0):
        self.__R = R
    
    def get_resistance(self):
        return self.__R
    
    def set_resistance(self, R: float):
        self.__R = R

def series(a: Resistor, b: Resistor) -> Resistor:
    Ra = a.get_resistance()
    Rb = b.get_resistance()
    return Resistor(Ra+Rb)

def parallel(a: Resistor, b: Resistor) -> Resistor:
    Ra = a.get_resistance()
    Rb = b.get_resistance()
    Rz = 1/(1/Ra + 1/Rb)
    return Resistor(Rz)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("R1", type=float)
    parser.add_argument("R2", type=float)
    args = parser.parse_args()

    a = Resistor(args.R1)
    b = Resistor(args.R2)
    print("Szeregowo:", series(a, b).get_resistance())
    print("Równolegle:", parallel(a, b).get_resistance())