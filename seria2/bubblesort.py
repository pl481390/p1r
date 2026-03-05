import sys

def bubble_sort(lista):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                swapped = True
    return lista

if __name__ == "__main__":
    lista = sys.argv[1:]
    print(bubble_sort(lista))
        
