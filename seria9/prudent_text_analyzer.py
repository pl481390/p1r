import argparse
from collections import Counter

class EmptyFileError(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class TextAnalyzer:
    def __init__(self) -> None:
        self.licznik = {}
    
    def load_file(self, filepath: str) -> None:
        try:
            input_file = open(filepath, "r")
            try:
                self.content = input_file.read()
                if self.content == "":
                    raise EmptyFileError("Pusty plik!")
            finally:
                input_file.close()
        except FileNotFoundError:
            raise FileNotFoundError(f"Nie znaleziono pliku {filepath}")
    
    def _count_words(self) -> dict[str, int]:
        #clean_text = [word.lower() for word in self.content.split() if word.isalpha()]
        #^Tutaj trzeba poprawić bo wywala słowa ze zanakami interpunkcyjnymi
        clean_text = []
        for word in self.content.split():
            output = ""
            for znak in word:
                if znak.isalpha():
                    output += znak.lower()
            clean_text.append(output)
        counter = Counter(word for word in clean_text)
        return dict(counter)
    
    def get_word_count(self, word: str) -> int:
        if not self.licznik:
            self.licznik = self._count_words()
        try:
            return self.licznik[word]
        except KeyError as e:
            print(f"Brak słowa {e}")
            return 0


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=str)
    parser.add_argument("word", type=str)
    args = parser.parse_args()

    analyzer = TextAnalyzer()
    analyzer.load_file(args.filepath)
    print(analyzer.get_word_count(args.word))