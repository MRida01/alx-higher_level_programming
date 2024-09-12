#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    name = dir(hidden_4)
    for i in range(len(name)):
        if name[i][0] != "_" and name[i][1] != "_":
            print(name[i])
