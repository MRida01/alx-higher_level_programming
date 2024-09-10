#!/usr/bin/python3

def print_battery_street(value):
    try:
        number = int(value)
        print(f"{number} Battery street")
    except ValueError:
        print("Error: Input must be an integer.")
