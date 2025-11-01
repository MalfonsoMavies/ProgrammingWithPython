while True:
    try:
        x, text = input().split()
        num = str(int(x))
        print(text + " " + num)
    except EOFError:
        break
