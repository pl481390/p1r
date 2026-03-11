import math
import sys
import matplotlib.pyplot as plt

def arctg(x, n):
    suma = 0
    for k in range(n):
        suma += (-1)**k * x**(2*k+1)/(2*k+1)
    return suma

if __name__ == "__main__":
    n = int(sys.argv[1])
    pi_lista = []
    for k in range(1, n+1):
        pi_lista.append(4*(4*arctg(1/5, k) - arctg(1/239, k)))
        print(k, pi_lista[k-1])
    plt.scatter(range(1, n+1), pi_lista)
    plt.plot(range(n+1), [math.pi for _ in range(n+1)])
    plt.title(f"Oszacowanie $\pi$ dla K = {n}")
    plt.show()
