while True:
    try:
        x, y = map(int, input().split())
        if x < y:
            print("Yes")
        else:
            print("No")
    except EOFError:
        break
