import math


def bmi(w, h):
    return h / math.pow(w, 2)


while True:
    try:
        w, h = map(float, input().split())
        bmi_value = bmi(w, h)
        if bmi_value < 18.5:
            print("underweight")
        elif 18.5 <= bmi_value < 25:
            print("normal weight")
        elif 25 <= bmi_value < 30:
            print("overweight")
        elif bmi_value >= 30:
            print("obese")
    except EOFError:
        break
