#!/usr/bin/python3

def raise_exception():
    try:
        month = January
        latest = month + 2
    except TypeError as e:
        raise e