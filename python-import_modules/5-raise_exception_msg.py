#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        message = ""
    except NameError as ne:
        raise ne
    print(ne)