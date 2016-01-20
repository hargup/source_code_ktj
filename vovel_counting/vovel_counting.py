#!/usr/bin/python
try:
    input = raw_input
except NameError:
    pass


def count(text):
    volves = ['a', 'e', 'i', 'o', 'u']
    text = text.lower()
    return sum([(s in volves) for s in text])


if __name__ == "__main__":
    text = input()
    print(count(text))
