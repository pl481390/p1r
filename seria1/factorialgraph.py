import factorials as f
import sys
import matplotlib.pyplot as plt
import timeit

if __name__ == "__main__":
    n = int(sys.argv[1])
    isilnie = []
    iczasy = []
    rsilnie = []
    rczasy = []
    for k in range(1, n+1):
        isilnie.append(f.ifactorial(k))
        itime = timeit.timeit("f.ifactorial(k)", globals=globals())
        iczasy.append(itime)
        
        rsilnie.append(f.rfactorial(k))
        rtime = timeit.timeit("f.rfactorial(k)", globals=globals())
        rczasy.append(rtime)
    
    plt.scatter(range(1, n+1), isilnie)
    plt.scatter(range(1, n+1), iczasy)
    plt.title("Iteracyjnie")
    plt.show()
    
    plt.scatter(range(1, n+1), rsilnie)
    plt.scatter(range(1, n+1), rczasy)
    plt.title("Rekurencyjnie")
    plt.show()
