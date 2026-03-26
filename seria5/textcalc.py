import argparse

def TextCalc(input_string):
    func_dict = {
        '+': lambda a,b:a+b,
        '-': lambda a,b:a-b,
        '*': lambda a,b:a*b,
        '/': lambda a,b:a/b,
        '%': lambda a,b:a%b,
        '^': lambda a,b:a**b
    }
    parts = input_string.split()
    a = float(parts[0])
    b = float(parts[2])
    return func_dict[parts[1]](a,b)

def calculate_file(nazwa_in, nazwa_out):
    with (
        open(nazwa_in, "r") as input_file,
        open(nazwa_out, "w") as output_file
    ):
        for line in input_file:
            output_string = line[:-1]
            output_string += " = "
            output_string += str(TextCalc(line))
            output_string += "\n"
            output_file.write(output_string)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()
    
    calculate_file(args.input, args.output)
