import argparse
import string

def ceasar(n, tekst):
	#kody = [ord(tekst[i]) for i in range(len(tekst))]
	#for kod in kody:
	    #if kod in range(ord('A'), ord('Z')+1) or kod in range(ord('a'), ord('z')+1):
	        #kod += n
	        #if kod not in range(ord('A'), ord('Z')+1) and kod not in range(ord('a'), ord('z')+1):
	            #if n > 0:
	                #kod -= 26
	            #else:
	                #kod += 26
	#output = "".join([chr(kody[i]) for i in range(len(kody))])
	output = ""
	for znak in tekst:
	    if znak.isalpha():
	        if znak in string.ascii_lowercase:
	            base = ord('a')
	        if znak in string.ascii_uppercase:
	            base = ord('A')
	        output += chr(ord(znak) - base + n %26 + base)
	    else:
	        output += znak
	return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', type=str)
    parser.add_argument('-n', '--shift', type=int)
    parser.add_argument('-t', '--text', type=str)
    args = parser.parse_args()
    print(args.text)
    
    if args.mode == "encrypt":
        print(ceasar(args.shift, args.text))
    if args.mode == "decrypt":
        print(ceasar(-args.shift, args.text))
