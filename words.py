

def print_upper_words(words):
    """Prints out each word in uppercase"""
    for word in words:
        print(word.upper())

print_upper_words(['bath', 'baby', 'bottle', 'beach', 'cow', 'computer'])


def print_upper_words2(words):
    """Prints out each word in uppercase if it starts with e or E"""
    for word in words:
        if word[0] == "e" or word[0] == "E":
            print(word.upper())
        else:
            print(word)
        

print_upper_words2(['bath', 'baby', 'bottle', 'elephant', 'Envelope','beach', 'cow', 'computer'])


def print_upper_words3(words, start_with):
    """Prints out each word in uppercase"""
    for word in words:
        for char in start_with:
            if word.startswith(char):
                print(word.upper())
        

print_upper_words3(['bath', 'baby', 'bottle', 'elephant', 'Envelope','beach', 'cow', 'computer'], "E")

