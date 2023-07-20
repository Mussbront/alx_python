#!/usr/bin/env python3
def validate_password(password):
    if len(password) < 8:
        return False
    
    upper = 0
    lower = 0
    digits = 0
    for character in password:
        if character.isupper():
            upper += 1
        elif character.islower():
            lower += 1
        elif character.isdigit():
            digits += 1
    if upper == 0 or lower == 0 or digits == 0:
        return False

    if " " in password:
        return False
    return True