import math

def sum_a(x, n):
    suma = 0
    for k in range(n+1):
        suma += (x**k)/math.factorial(k)
    return suma

def sum_b(x, n):
    suma = 0
    for k in range(n+1):
        suma += (-1)**k * x**(2*k)/math.factorial(2*k)
    return suma

if __name__ == "__main__":
    x = float(input("x = "))
    n = int(input("n = "))
    print("sum_a(x, n) = ", sum_a(x, n))
    print("sum_b(x, n) = ", sum_b(x, n))
