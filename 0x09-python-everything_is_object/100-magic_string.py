#!/usr/bin/python3
def magic_string():
    return ", ".join(["BestSchool"] * magic_string.calls())
magic_string.calls = lambda: magic_string.__dict__.setdefault("counter", 0) + 1
