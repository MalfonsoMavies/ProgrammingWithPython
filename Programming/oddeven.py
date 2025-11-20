while True:
    try:
        x = int(input())
        if x % 2 == 0:
            print("even")
        else:
            print("odd")
    except EOFError:
        break
