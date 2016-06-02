def word_frequency (words):
    """Returns frequency of each word given a list of words.

        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    frequency = {}
    for w in words:
        frequency[w] = frequency.get (w, 0) + 1
    return frequency

def read_words (filename):
	return [x.strip ('.,:;!?()[]\{\}`"\'<>/') for x in open (filename).read ().split ()]

def main (filename):
    frequency = word_frequency (read_words (filename))
    ordered_frequency = sorted (frequency, key = lambda x : frequency[x], reverse = True)
    for word in ordered_frequency:
        print word, frequency[word]

if __name__ == "__main__":
    import sys
    main (sys.argv[1])