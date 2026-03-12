import collections
import sys

def liczenie(lista):
    counter = collections.Counter(lista)
    #sorted_counter = {key: value for key, value in sorted(counter.values())}
    print(counter)

if __name__ == "__main__":
    lista = sys.argv[1:]
    liczenie(lista)
