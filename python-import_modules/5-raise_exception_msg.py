#!/usr/bin/python3

def raise_exception_msg(message=""):
    raise NameError(message)
try:
    raise_exception_msg()
except NameError as ne:
    raise ne
print(ne)