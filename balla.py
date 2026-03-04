import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--radius', type=float)
args = parser.parse_args()
R = args.radius

pole = 4*math.pi*R**2
obj = (4*math.pi*R**3)/3

print(f"Pole powierzchni: {pole}")
print(f"Objętość: {obj}")