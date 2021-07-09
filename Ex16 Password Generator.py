import random
import string

def genPassword(n):
    source = string.ascii_letters + string.digits + string.punctuation
    print(''.join([random.choice(source) for i in range(n)]))

pwlength = int(input("How many characters in your Password? "))
genPassword(pwlength)