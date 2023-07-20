#!/usr/bin/python3
for n in range(9):
    for j in range(n + 1, 10):
        if n * 10 +j <= 88:
            print("{:02}".format(n * 10 + j), end=", ")
        elif n * 10 + j == 90:
            print("{:02}".format(n * 10 + j), end="\n")
        else:
            print("{:02}".format(n * 10 + j), end="")