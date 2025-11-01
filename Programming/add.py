def add(x, y):
    return x + y


while True:
    try:
        x, y = map(int, input().split())
        print(add(x, y))
    except EOFError:
        break
