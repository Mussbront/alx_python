#!/usr/bin/python3

import sys

def main():
    
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 1:
        print("{} argument:".format(num_arguments), end="\n")
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg), end="\n")
    elif num_arguments > 1:
        print("{} arguments:".format(num_arguments), end="\n")
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg), end="\n")
    elif num_arguments == 0:
        print("{} arguments.".format(num_arguments), end="\n")

if __name__ == "__main__":
    main()