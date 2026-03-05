import sys
import collections

def most_frequent(lista):
    counter = collections.Counter(lista)
    max_count = max(counter.values())
    wynik = [(item, count) for item, count in counter.items() if count == max_count]
    return wynik

#def most_frequent_naive(lista):
    
    
if __name__ == "__main__":
    lista = sys.argv[1:]
    print(most_frequent(lista))
