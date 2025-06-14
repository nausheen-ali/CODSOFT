import random
import string

len=int(input("Enter desired length of password:"))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

password = ""

for i in range(len):
    '''next_char = random.choice(chars)
    password += next_char'''
    password += random.choice(chars)

print ("Your password is: ",password)