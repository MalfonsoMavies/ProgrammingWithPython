while True:
    try:
        x = int(input())
        print(x)
    except EOFError:
        break