import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = b**2 - 4*a*c

if delta >= 0:
    rozw1 = (-b + math.sqrt(delta))/(2*a)
    rozw2 = (-b - math.sqrt(delta))/(2*a)
else:
    rozw1 = (complex(-b, math.sqrt(-delta)))/(2*a)
    rozw2 = (complex(-b, -math.sqrt(-delta)))/(2*a)

print(rozw1)
print(rozw2)