import string
try:
    input = raw_input
except NameError:
    pass


def caesar(plaintext, shift):
    plaintext = plaintext.lower()
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


if __name__ == "__main__":
    text = input()
    print(caesar(text, 4))
