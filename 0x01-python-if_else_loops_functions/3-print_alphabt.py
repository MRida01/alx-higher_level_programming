#!/usr/bin/python3

print(
    "".join(
        [chr(char) for char in range(ord('a'), ord('z') + 1) if chr(char) not in 'qe']
    ).format(), end=""
)
