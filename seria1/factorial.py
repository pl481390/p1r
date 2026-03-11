import factorials as f
import timeit
import sys

if __name__ == "__main__":
    n = int(sys.argv[1])
    itime = timeit.timeit("f.ifactorial(n)", globals=globals())
    print("Iteracyjnie: ", f.rfactorial(n), "t = ", itime)
    rtime = timeit.timeit("f.rfactorial(n)", globals=globals())
    print("Rekurencyjnie: ", f.rfactorial(n), "t = ", rtime)
