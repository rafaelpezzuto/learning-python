def char_frequency (chars):
    frequency = {}
    for caractere in chars:
        frequency[caractere] = frequency.get (caractere, 0) + 1
    return frequency

def read_chars (filename):
    palavras = [palavra.strip(".,;:!@#$%^&*~`{}[]()?|\\") for palavra in open(filename).read ().split ()]
    palavras = [palavra.replace("'", "") for palavra in palavras]

    return [item for sublist in palavras for item in sublist]

def main (filename):
    frequency = char_frequency (read_chars (filename))
    ordered_frequency = sorted (frequency, key = lambda x : frequency[x], reverse = True)
    for caractere in ordered_frequency:
        print caractere, frequency[caractere]

if __name__ == "__main__":
    import sys
    main (sys.argv[1])