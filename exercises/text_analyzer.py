import re

class TextAnalyzer(object):

    def __init__(self, text):
        text = re.sub(r"[\W]", ' ', text)
        text = re.sub(r"[\s]+", ' ', text)
        self.text = text.lower()
        self.d = None

    def freqAll(self):
        self.d = dict()
        words = self.text.split()
        for word in words:
            if word in self.d:
                self.d[word] = self.d[word] + 1
            else:
                self.d[word] = 1
    
    def freqOf(self, word):
        if self.d is None:
            self.freqAll()

        if word in self.d:
            return self.d[word]
        else:
            return 0


ta = TextAnalyzer("test123.?? Hello ?? World !! apple banana banana coconut")
print(ta.freqOf('cider'))

print(ta.freqOf('banana'))