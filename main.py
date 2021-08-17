import random
import string

letter = string.ascii_letters
digits = string.digits
symbol = string.punctuation

print("Python Password Generator\n")

def generate():
    length = int(input("the Length of your password: "))
    combine = letter + digits + symbol
    sample = random.sample(combine, length)

    password = "".join(sample)
    print(password)

generate()
