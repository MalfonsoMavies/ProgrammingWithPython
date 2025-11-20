while True:
    try:
        x = int(input())
        if x >= 4 and x <= 11:
            print("Good morning")
        elif x >= 12 and x <= 17:
            print("Good afternoon")
        elif x >= 18 and x <= 23:
            print("Good evening")
        else:
            print("Hi")
    except EOFError:
        break
