#!/usr/bin/python3

def uppercase(string):
    for c in string:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - ord('a') + ord('A'))
            print("{}".format(c), end="")
            print()
