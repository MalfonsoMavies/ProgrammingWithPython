def triple(x):
    return 3 * x


while True:
    try:
        x = input()
        print(triple(int(x)))
    except EOFError:
        break
