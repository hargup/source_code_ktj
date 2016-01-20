#!/usr/bin/python
try:
    input = raw_input
except NameError:
    pass


def reverse(string):
    return string[::-1]


def swap_halfs(string):
    n = len(string)
    if n % 2 == 0:
        return string[n//2:] + string[:n//2]
    else:
        return string[n//2+1:] + string[n//2] + string[:n//2]


def permu(string):
    return reverse(swap_halfs(string))

if __name__ == "__main__":
    string = input()
    print(permu(string))
