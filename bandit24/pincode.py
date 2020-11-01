#!/usr/bin/python3
import random

pin_code = []
password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

for x in range(4):
        pin_code.append(random.randint(0, 9))

result = ""

for x in range(4):
    result += str(pin_code[x])

print(password + " " + result)

