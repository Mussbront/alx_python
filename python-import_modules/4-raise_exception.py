#!/usr/bin/python3

def raise_exception():
    try:
        current_month = 'January'
        next_payment = current_month + 3
    except TypeError as e:
        raise e