import sys

def is_palindrome(wyrazenie: str | list):
	if(isinstance(wyrazenie, list)):
		wyrazenie = "".join(wyrazenie)
	wyrazenie = "".join(wyrazenie[i] for i in range(len(wyrazenie)) if wyrazenie[i].isalpha())
	return wyrazenie.lower() == wyrazenie[::-1].lower()

if __name__ == "__main__":
    print(is_palindrome(sys.argv[1:]))
