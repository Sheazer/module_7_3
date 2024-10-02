
class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        symbols = ',.=!?:;-'
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                x = file.read()
                x = x.lower()
                for symbol in symbols:
                    x = x.replace(symbol, '')
                    all_words[i] = x.split()
        return all_words

    def count(self, word):
        lib = {}
        for name, words in self.get_all_words().items():
            count = 0
            for i in words:
                if word.lower() == i:
                    count += 1
            lib[name] = count
        return lib

    def find(self, word):
        lib = {}
        for name, words in self.get_all_words().items():
            count = 0
            for j, i in enumerate(words):
                if word.lower() == i:
                    count = j+1
                    break
            lib[name] = count
        return lib


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))