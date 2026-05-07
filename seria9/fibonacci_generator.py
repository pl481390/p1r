import argparse

class FibIterator:
    def __init__(self):
        self.previous = 0
        self.current = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.current
        self.previous,self.current = self.current,self.current+self.previous
        return result


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("liczba", type=int)
    args = parser.parse_args()

    iterator = FibIterator()
    for x in iterator:
        if x>args.liczba:
            print(x)
            break