#!/usr/bin/python3
for ch in range(97, 123):
    if ch not in (101, 113):
        print("{}".format(chr(ch)), end='')
