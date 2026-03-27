import argparse

def enigma_encrypt(klucz, nazwa_in, nazwa_out):
    with (
        open(nazwa_in, "r") as input_file,
        open(nazwa_out, "w") as output_file
    ):
        for line in input_file:
            for znak in line:
                output_file.write(str(ord(znak)^klucz))
                output_file.write(" ")

def enigma_decrypt(klucz, nazwa_in, nazwa_out):
    with (
        open(nazwa_in, "r") as input_file,
        open(nazwa_out, "w") as output_file
    ):
        for line in input_file:
            kody = line.split()
            for kod in kody:
                output_file.write(chr(int(kod)^klucz))
                

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--encrypt", action="store_true")
    group.add_argument("-d", "--decrypt", action="store_true")
    parser.add_argument("key")
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()
    
    if args.encrypt:
        enigma_encrypt(int(args.key), args.input, args.output)
    if args.decrypt:
        enigma_decrypt(int(args.key), args.input, args.output)
