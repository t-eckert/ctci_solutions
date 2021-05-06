"""
  16.2 Word Frequencies: Design a method to find the frequency of occurrences
    of any given word in a book.
"""
import string

test_book = "Simple is the way. Things are going to be grand. I am telling you, buddy. They will be grand."


def open_book(filename):
    book = ""
    text = open(filename)
    for line in text:
        book += " " + line
    return book


def count_wordFrequency(book):
    word_frequency = {}
    translator = str.maketrans("", "", string.punctuation)
    book = book.translate(translator).lower().split()
    for word in book:
        if word not in word_frequency.keys():
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1
    return word_frequency


def main():
    print(count_wordFrequency(open_book("q2_testFile.txt")))
    pass


main()
