#!/usr/bin/python3

#Generate a random password of any desired length and any desired number of passwords.
#Usage: python ./passwordgen.py 
#This script was created on Linux using VIM. 

import random 

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789!@#$%&-_=+?!@#$%&-_=+?'

length = input('password length? ')
length = int(length)

number = input('number of passwords? ')
number = int(number)
 

for p in range(number):
    password = ''
    for c in range(length):
      password += random.choice(chars)
    print(password)
