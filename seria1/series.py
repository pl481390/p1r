import sums
import sys

if __name__ == "__main__":
    x = float(sys.argv[1])
    n = int(sys.argv[2])
    print("sum_a(x, n) = ", sums.sum_a(x, n))
    print("sum_b(x, n) = ", sums.sum_b(x, n))
