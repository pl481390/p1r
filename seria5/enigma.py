import argparse

def enigma_encrypt(klucz, nazwa_in, nazwa_out):
    with (
        open(nazwa_in, "r") as input_file,
        open(nazwa_out, "w") as output_file
    ):
        for line in input_file:
            for znak in line:
                output_file.write(ord(znak)^klucz)
                output_file.write(" ")

def enigma_decrypt(klucz, nazwa_in, nazwa_out):
    

if __name__ == "__main__":
    
