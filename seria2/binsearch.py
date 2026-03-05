import sys

def bin_search(szukany, lista, min, max):
    lista.sort()
    while True:
        if min == max:
            if lista[min] == szukany:
                return min
            else:
                return -1
        elif lista[(min+max)//2] < szukany:
            min = (min+max)//2
        else:
            max = (min+max)//2

if __name__ == "__main__":
    szukany = int(sys.argv[1])
    lista = (input("lista = ")).split(" ")
    lista = [int(element) for element in lista]
    print(bin_search(szukany, lista, 0, len(lista)-1))
