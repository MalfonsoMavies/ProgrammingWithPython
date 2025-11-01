def inc(x):
    return x + 1


while True:
    try:
        x = int(input())
        print(inc(x))
    except EOFError:
        break
