import argparse

def sumuj_ceny(filename):
    suma = 0
    with (
        open(filename, "r") as input_file
    ):
        for line in input_file:
            suma += float(line.rsplit()[-1])
    return suma
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    
    print(sumuj_ceny(args.filename))
    
