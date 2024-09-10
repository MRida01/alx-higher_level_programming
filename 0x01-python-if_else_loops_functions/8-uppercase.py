#!/usr/bin/python3
def uppercase(s):
    for char in s:
        upper_char = chr(ord(char) - (ord('a') - ord('A')))
        if 'a' <= char <= 'z' else char
        print("{}".format(upper_char), end="")
    print()


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
