import random

if __name__ == "__main__":
    liczby = set()
    while len(liczby) < 6:
        liczby.add(random.randint(1, 49))
    
    print(liczby)
