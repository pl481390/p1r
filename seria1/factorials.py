def ifactorial(n):
    wynik = 1
    for k in range(2, n+1):
        wynik *= k
    return wynik

def rfactorial(n):
    if n in [0, 1]:
        return 1
    else:
        return n*rfactorial(n-1)

if __name__ == "__main__":
    n = int(input("n = "))
    print("ifactorial(n) = ", ifactorial(n))
    print("rfactorial(n) = ", rfactorial(n))
