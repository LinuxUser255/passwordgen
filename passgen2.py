#!/usr/bin/env python3

import string
import secrets

length = int(input("Password length: "))

def password_generator(length):
    password = ''  # empty string
    for i in range(length):
        password += secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.ascii_uppercase)
        password += secrets.choice(string.digits)
        password += secrets.choice(string.punctuation)

    return password  # returns the string

print(password_generator(length))
