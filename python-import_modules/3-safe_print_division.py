#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result), end="\n")
        print("{:d} / {:d} = {}".format(a, b, result), end="\n")
    
safe_print_division(8, 0)