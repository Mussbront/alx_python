#!/usr/bin/python3

def raise_exception_msg(message=""):
    raise NameError(message)
try:
    raise_exception_msg(message="")
except NameError as e:
    raise e