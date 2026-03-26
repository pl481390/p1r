import argparse

def remove_comment(znak, nazwa_in, nazwa_out):
    with (
        open(nazwa_in, "r") as input_file,
        open(nazwa_out, "w") as output_file
    ):
        for line in input_file:
            if not line.strip().startswith(znak):
                output_file.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('znak')
    parser.add_argument('nazwa_in')
    parser.add_argument('nazwa_out')
    args = parser.parse_args()
    
    remove_comment(args.znak, args.nazwa_in, args.nazwa_out)
