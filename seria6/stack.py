import argparse

class Stack:
    def __init__(self):
        self._stack: list = []
    
    def push(self, element) -> None:
        self._stack.append(element)

    def is_empty(self) -> bool:
        if len(self._stack) == 0:
            return True
        else:
            return False
    
    def pop(self):
        output = self._stack.pop()
        return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", nargs='+', type=float)
    args = parser.parse_args()

    stack = Stack()
    for element in args.numbers:
        stack.push(element)
    while not stack.is_empty():
        print(stack.pop())