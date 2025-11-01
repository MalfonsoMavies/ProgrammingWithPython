import math


def calculateCircumference(r):
    return 2 * math.pi * r


def calculateArea(r):
    return math.pi * pow(r, 2)


while True:
    try:
        r = float(input())
        if r > 0:
            print(f"{calculateCircumference(r):.2f} {calculateArea(r):.2f}")
    except EOFError:
        break
