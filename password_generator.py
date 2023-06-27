''' Password generator project and Github project'''

# import a built in python
# library called random

import random

print("Password Generator Program")

# a variable with characters to enhance a strong and unique password to be produced
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

# variable for how many passwords to be generated
number = input('Amount of passwords to generate: ')

number = int(number)

length = input('Input password length: ')

length = int(length)
print('\nYour passwords are below:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

