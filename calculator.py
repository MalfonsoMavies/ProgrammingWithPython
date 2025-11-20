import math


def computeSinInDegrees(angle_in_degrees):
    return math.sin(math.radians(angle_in_degrees))


def computeCosInDegrees(angleInDegrees):
    return math.cos(math.radians(angleInDegrees))


def computeRadians(angleInDegrees):
    return angleInDegrees * (math.pi / 180)


def addition(x, y):
    return x + y


def Subtraction(x, y):
    return x - y


def Multiplication(x, y):
    return x * y


def Division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Division by 0 errror!"


def Power(x, y):
    return x**y


def Modulus(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return "Division by 0 error!"


def SquareRoot(InputNumber):
    return InputNumber ** (1 / 2)


def ComputeAbsoluteValue(distance):
    if distance < 0:
        return -distance
    else:
        return distance


def SimpleLog(base, input):
    lower_bound = 0
    cursor = input / base
    while cursor >= 1:
        cursor = cursor / base
        lower_bound += 1

    return lower_bound


def Logarithm(base, input):
    lower_bound = SimpleLog(base, input)
    upper_bound = lower_bound + 1

    approximation = (lower_bound + upper_bound) / 2

    number_guess = base**approximation

    precision = 0.0001
    while number_guess - input > precision:

        if number_guess == input:
            return approximation
        elif number_guess > input:
            upper_bound = approximation
        else:
            lower_bound = approximation

        approximation = (lower_bound + upper_bound) / 2

        number_guess = base**approximation

    return approximation


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def eFunction(x, approximation_terms):
    result = 0
    for i in range(approximation_terms):
        result += (x**i) / factorial(i)
    return result


def sin(x, approximation_terms):
    sum = 0
    sign = 1
    for i in range(1, approximation_terms, 2):
        sum = sign * (x**i) / factorial(i) + sum
        sign = -sign
    return sum


def cos(x, approximation_terms):
    sum = 0
    sign = 1
    for i in range(0, approximation_terms, 2):
        sum = sign * (x**i) / factorial(i) + sum
        sign = -sign
    return sum


x, y = map(float, input().split())

calculation = input().strip()

match calculation:
    case "+":
        print(addition(x, y))

    case "-":
        print(Subtraction(x, y))

    case "*":
        print(Multiplication(x, y))

    case "/":
        rounded_division = round(Division(x, y), 2)
        print(rounded_division)

    case "%":
        print(Modulus(x, y))

    case "^":
        print(Power(x, y))

    case "sqrt":
        rounded_sqrt_x = round(SquareRoot(x), 2)
        rounded_sqrt_y = round(SquareRoot(y), 2)
        print(rounded_sqrt_x)
        print(rounded_sqrt_y)

    case "abs":
        abs_x = ComputeAbsoluteValue(x)
        abs_y = ComputeAbsoluteValue(y)
        print(abs_x)
        print(abs_y)

    case "l":
        base = float(input())
        print(round(Logarithm(base, x), 2))
        print(round(Logarithm(base, y), 2))

    case "exp":
        approximation_terms = int(input())
        print(eFunction(x, approximation_terms))
        print(eFunction(y, approximation_terms))

    case "!":
        print(factorial(int(x)))
        print(factorial(int(y)))

    case "sin":
        approximation_terms = int(input())
        radiansx = round(computeRadians(x), 2)
        radiansy = round(computeRadians(y), 2)
        print(round(sin(radiansx, approximation_terms), 2))
        print(round(sin(radiansy, approximation_terms), 2))

    case "cos":
        approximation_terms = int(input())
        radiansx = round(computeRadians(x), 2)
        radiansy = round(computeRadians(y), 2)
        print(round(cos(radiansx, approximation_terms), 2))
        print(round(cos(radiansy, approximation_terms), 2))
